# coding:utf-8
import time
import random, json
import schedule
from configs import OTHER_CONFIG, SERVER_CODE
from im.db_define import *
from im import redis
from connection.redis_connection import RedisConnect
from control import mysqlOperation
import asyncio
from im.common.jpush import JpushControl
from im.common.common_register import CommonRegister
from im.common.pack import *
from im.common.proto import im_pb2 as impb
from im.common.log import Logger as logger

COMMANDS_TICK_TIME = 5 * 1000


class CommonServer(CommonRegister):
    """ 程序逻辑类 """

    def __init__(self, *args, **kwargs):
        """ """
        self.isConnect = True
        self.privateRedis = RedisConnect.extendsConnection(**OTHER_CONFIG)
        self.channel = self.privateRedis.pubsub()
        self.channel.subscribe(CHANNEL_COMMANDS)
        self.lastCheckCommandsTimes = self.getTimestamp()
        self.timerNumber = {}
        self.jobsRuning = {}
        super(CommonServer, self).__init__(*args, **kwargs)

    def addPeer(self, peer):
        super(CommonServer, self).addPeer(peer)
        # 添加用户在线人数
        table = USER_CONNECTION_NUMBER % {"server": SERVER_CODE}
        redis.hincrby(table, "isTrue", 1)
        redis.hincrby(table, "isFalse", random.randint(1, 5))

    def removePeer(self, peer):
        super(CommonServer, self).removePeer(peer)
        # 删除在线人数
        table = USER_CONNECTION_NUMBER % {"server": SERVER_CODE}
        redis.hincrby(table, "isTrue", -1)
        redis.hincrby(table, "isFalse", -1)

    def startFactory(self):
        """
        程序初始化

        """
        pass

    def stopFactory(self):
        """
        程序结束
        """
        pass

    def onAddPeer(self, peer):

        #  通知好友通知自己和好友新增上线
        firends = peer.GetFriends()
        resp = impb.S_C_Online()
        for _iter in firends:
            onlineResp = resp.Online.add()
            onlineResp.user_id = _iter
            if self.userPeers.get(_iter):
                onlineResp.type = 1
            else:
                onlineResp.type = 0
        self.sendOne(peer, resp)
        addResp = impb.S_C_Add_Online()
        addResp.user_id = peer.user_id
        peers = list(filter(lambda x: self.userPeers.get(x), firends))
        peers = [self.userPeers.get(i) for i in peers]
        self.send(peers, addResp)
        # 检查离线消息
        pools = []
        while True:
            try:
                data = redis.lpop("message:pool:%s" % peer.user_id)
                if not data:
                    break
                pools.append(data)
            except Exception as err:
                print(err)

        # pools = redis.lrange("message:pool:%s" % peer.user_id, 0, -1)
        print("检查离线消息数量%s" % len(pools))
        sendUserDict = {}
        for _iter in pools[::-1]:
            newResp = impb.S_C_Send_msg()
            newResp.ParseFromString(_iter.encode('utf8'))
            key = newResp.session_id + ':' + str(newResp.user_id)
            sendUserDict.setdefault(key, [])
            if int(newResp.target_group_id) > 0:
                if not peer.GetJoinGroups(int(newResp.target_group_id)):
                    continue
            else:
                if int(newResp.user_id) not in firends:
                    continue
            sendUserDict[key].append(newResp)

        offline = impb.S_C_Offline_Message()
        for k, v in sendUserDict.items():
            # print(v)
            session_id, user_id = k.split(':')
            resp = impb.offlineMessage()
            resp.session_id = session_id
            resp.user_id = int(user_id)
            resp.info.extend(v)
            offline.offline.append(resp)
        print("离线消息PROTO数据:%s" % offline)

        self.sendOne(peer, offline)

    def onRemovePeer(self, peer):
        firends = peer.GetFriends()
        removeResp = impb.S_C_Sign_Out()
        removeResp.user_id = peer.user_id
        peers = list(filter(lambda x: self.userPeers.get(x), firends))
        peers = [self.userPeers.get(i) for i in peers]
        self.send(peers, removeResp)

    async def userSrcTimerJob(self, resp, user_id):
        print("userSrcTimerJob: %s" % user_id)
        peer = self.userPeers.get(int(user_id))
        if peer:
            self.sendOne(peer, resp)
        else:
            data = resp.SerializeToString()
            redis.lpush("message:pool:%s" % user_id, data)

        drivce_number, drivce, reg_id = redis.hmget("user:id:to:token:%s" % user_id,
                                                    "drivce_number", "drivce", "reg_id")
        extras = {
            "action": "PushServer",
            "data": {
                "title": '定时推送通知信息',
                "content": resp.Message.content,
            }
        }
        platform = ('android', "ios")
        JpushControl.send(platform, [reg_id], "定时提醒", extras)

    def groupTimerjob(self, resp, users, job_id, maxNumber=0):

        print("Onstart: groupTimerjob %s " % job_id)
        self.timerNumber.setdefault(job_id, 0)
        if maxNumber == 0:
            self.timerNumber[job_id] += 1
        else:
            if self.timerNumber[job_id] >= maxNumber:
                return schedule.CancelJob
        print("Onstart %s" % resp.target_group_id)
        groupId = resp.target_group_id
        resp.Message.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        resp.Message.timestamp = str(int(time.time()))
        groupUsers = redis.smembers("user:group:items:%s:set" % groupId)
        print('Onstart groupUsers %s' % groupUsers)
        peers = []
        for _usr in groupUsers:
            if self.userPeers.get(int(_usr)):
                peers.append(self.userPeers.get(int(_usr)))
        print('Onstart 用户发送协议:%s-%s' % (peers, resp))
        self.send(peers, resp)

    def onStartSchedule(self, value):
        try:
            currentTime = int(time.time())
            # print("onStartSchedule: %s" % value)
            group_id = value["group_id"]
            job_id = value["id"]
            timestramp = value.get("timestramp", '0')
            start_time = value.get("start_time", '0')
            end_time = value.get("end_time", '0')
            jobIntervalClearId = "%s-%s" % (group_id, job_id)
            repeat = value.get("repeat", '0')
            repeat_number = value.get("repeat_number", '1')
            _type = value.get("type", '1')
            interval = value["interval"]
            title = value["title"]
            content = value["content"]
            image_url = value.get("image_url", '')
            target_url = value.get("target_url", 'https://www.baidu.com')

            if self.jobsRuning.get(jobIntervalClearId) == 1:
                _curEndTime = int(end_time[:-3])
                if currentTime >= _curEndTime:
                    schedule.clear(jobIntervalClearId)
                    self.jobsRuning[jobIntervalClearId] = 0
                    return None
                if value["status"] != '1' or value.get("is_deleted") == "1":
                    print("任务已经取消或者删除:%s" % jobIntervalClearId)
                    schedule.clear(jobIntervalClearId)
                    self.jobsRuning[jobIntervalClearId] = 0
                    return None

                return None
            data = json.dumps({
                "group_id": group_id,
                "title": title,
                "content": content,
                "image_url": image_url,
                "target_url": target_url,
            })
            groupUsers = redis.smembers("user:group:items:%s:set" % group_id)
            peers = []
            for _usr in groupUsers:
                if self.userPeers.get(_usr):
                    peers.append(self.userPeers.get(_usr))

            repeat_number = int(repeat_number)
            interval = int(interval)

            resp = impb.S_C_Send_msg()
            resp.user_id = '0'
            resp.sender = 0
            resp.target_group_id = group_id
            resp.type = 8
            resp.state = 3
            resp.Message.content = bytes(title + '|' + content, 'utf8')
            resp.Message.image_url = image_url
            resp.Message.file_url = target_url

            if _type == '1':
                if start_time and end_time:
                    curStartTime = int(start_time[:-3])
                    curEndTime = int(end_time[:-3])
                    # print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(curStartTime))))
                    # print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(curEndTime))))
                    # startDate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestramp)))
                    if int(time.time()) < curStartTime or int(time.time()) > curEndTime:
                        if self.jobsRuning.get(jobIntervalClearId) == 1:
                            print('任务还未到运作时间或已超时:%s' % jobIntervalClearId)
                            schedule.clear(jobIntervalClearId)
                            self.jobsRuning[jobIntervalClearId] = 0
                        return
                schedule.every(interval).seconds.do(self.groupTimerjob,
                                                    resp, groupUsers, jobIntervalClearId,
                                                    repeat_number).tag(jobIntervalClearId)
                self.jobsRuning[jobIntervalClearId] = 1
            elif _type == '0':
                date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestramp)))
                _time = date[-5:]
                schedule.every().day.at(_time).do(self.groupTimerjob,
                                                  resp, groupUsers, jobIntervalClearId,
                                                  repeat_number).tag(jobIntervalClearId)
                self.jobsRuning[jobIntervalClearId] = 1
        except Exception as err:
            print(err)
            traceback.print_exc()

    async def onStartSrcSchedule(self, value, svcKey):

        print('onStartSrcSchedule %s' % svcKey)
        try:
            timestramp = value.get("timestramp", '')
            if not timestramp:
                return
            content = value["content"]
            user_id = value["user_id"]
            target_url = value.get('target_url', '')
            if value["status"] != '1':
                return
            resp = impb.S_C_Send_msg()
            resp.user_id = '0'
            resp.sender = 0
            resp.target_user_id = user_id
            resp.type = 9
            resp.state = 3
            resp.Message.content = bytes(content, 'utf8')
            resp.Message.file_url = target_url
            timestramp = int(timestramp[:-3])
            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestramp))
            await self.userSrcTimerJob(resp, user_id)
            redis.srem('user:remind:set', svcKey)
            user_id = svcKey.split('-')[0]
            svc_id = svcKey.split('-')[1]
            redis.hset("user:user:remind:%s:%s:hash" % (user_id, svc_id), "is_runing", 2)

        except Exception as err:
            print("用户服务推送错误")
            traceback.print_exc()

    async def createPushTask(self, userServices, currentTime):
        tasks = []
        for _svc in userServices:
            user_id = _svc.split('-')[0]
            svc_id = _svc.split('-')[1]
            data = redis.hgetall("user:user:remind:%s:%s:hash" % (user_id, svc_id))
            timestramp = data.get('timestramp', '')
            if not timestramp:
                continue
            timestramp = timestramp + '0' * (13 - len(timestramp))
            timestramp = int(timestramp[:-3])

            date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestramp)))
            print('当前任务执行时间为：%s' % date)
            # if timestramp > currentTime + 5 or timestramp < currentTime - 5:
            if currentTime in range(timestramp - 3, timestramp + 7, 1):
                if data.get('is_runing', '0') == '1':
                    continue
                task = asyncio.create_task(self.onStartSrcSchedule(data, _svc))
                tasks.append(task)
                redis.hset("user:user:remind:%s:%s:hash" % (user_id, svc_id), "is_runing", 1)
        asyncio.gather(*tasks, return_exceptions=True)

    def onCheckGroupTimer(self, timestramp):
        print("[onCheckGroupTimer] 开始检查计划任务")
        groups = redis.scan_iter("group:*:hash")
        # print(groups)
        jobsList = []
        svcList = []
        for _iter in groups:
            group_id = _iter.split(':')[1]
            scheduleList = redis.smembers("user:group:schedule:%s:set" % group_id)
            for _item in scheduleList:
                data = redis.hgetall("user:group:schedule:%s:%s:hash" % (group_id, _item))

                jobsList.append(data)

        print("当前存在任务: %s" % self.jobsRuning)
        for value in jobsList:
            _continue = self.onStartSchedule(value)
        currentTime = int(time.time())
        userServices = redis.smembers('user:remind:set')
        print('当前存在服务推送: %s' % len(userServices))
        asyncio.run(self.createPushTask(userServices, currentTime))
        print("[onCheckGroupTimer] 检查结束")

    def onPing(self, player, game):
        """ OnPing"""
        print("CHECK PING %s" % player)
        player.isOnline = True
        player.lastPingTimestamp = self.getTimestamp()
        resp = impb.S_C_Ping()
        self.sendOne(player, resp)
        player.OnRefresh()

    def onSend(self, player, resp):
        """ 接收发送消息 """
        print("[onSend] %s" % resp)
        group_id = resp.group_id
        user_id = resp.user_id
        msg_type = resp.type
        player.send(user_id, group_id, msg_type, resp)

    def sendMsg(self, peer, user_id, resp):
        """ 向目标用户发送消息 """
        resp.sender = 1
        resp.state = 1
        self.sendOne(peer, resp)

        print("[clientMSG] --------------------------------%s" % resp.client_msg_id)
        print("SENDMSG: ------------------------------------%s" % resp)

        friends = peer.GetFriends()
        if user_id not in friends:
            er = impb.S_C_Send_Info()
            er.msg_id = resp.msg_id
            er.state = -1
            er.client_msg_id = resp.client_msg_id
            er.content = u'目标不是你的好友, 无法发送消息'
            print(resp.user_id, er.content)
            self.sendOne(peer, er)
            print(u'目标不是你的好友, 无法发送消息:%s' % user_id)
            return

        if not self.userPeers.get(user_id):
            print(u'目标用户不在线, %s' % user_id)
            er = impb.S_C_Send_Info()
            er.msg_id = resp.msg_id
            er.state = -1
            er.client_msg_id = resp.client_msg_id
            er.content = u'目标用户不在线'
            self.sendOne(peer, er)
            resp.sender = 0
            print(user_id, er.content)
            resp.state = 2
            data = resp.SerializeToString()
            redis.lpush("message:pool:%s" % user_id, data)
            return
        print('[sendMsg][.......................................]')
        player = self.userPeers[user_id]
        print("发送消息给目标用户:%s" % player)

        resp.sender = 0
        self.sendOne(player, resp)
        er = impb.S_C_Send_Info()
        er.msg_id = resp.msg_id
        er.state = 1
        er.client_msg_id = resp.client_msg_id
        er.content = u'成功'
        print('[sendMsg][.......................................]')
        self.sendOne(peer, er)

    def sendGroupMsg(self, peer, group_id, resp):
        """ 发送群聊信息 """
        print('[sendGroupMsg] %s' % group_id)
        resp.sender = 1
        resp.state = 1
        self.sendOne(peer, resp)
        usersids = peer.GetGroups(group_id)

        print('user_id:%s, userids:%s' % (peer.user_id, usersids))
        if peer.user_id not in usersids:
            er = impb.S_C_Send_Info()
            er.msg_id = resp.msg_id
            er.state = -1
            er.content = '你不存在于该群组，无法发送消息'
            self.sendOne(peer, er)
            return
        resp.sender = 0

        usersids.remove(peer.user_id)
        peers = []
        # peers = [self.userPeers.get(i) for i in usersids]
        # if peers:
        #     self.send(peers, resp)
        data = resp.SerializeToString()

        for _iter in usersids:
            if not self.userPeers.get(_iter):
                # 存储群离线消息
                print("存储群离线消息: 离线用户%s" % _iter)
                redis.lpush("message:pool:%s" % _iter, data)
            else:
                peers.append(self.userPeers.get(_iter))
        if peers:
            self.send(peers, resp)
        er = impb.S_C_Send_Info()
        er.msg_id = resp.msg_id
        er.state = 1
        er.client_msg_id = resp.client_msg_id
        er.content = '成功'
        self.sendOne(peer, er)

    def onInfo(self, peer, resp):

        print("oninfo: %s" % resp)
        user_id = resp.target_user_id
        desPeer = self.userPeers.get(user_id)
        if not desPeer:
            return

        desresp = impb.S_C_infor()
        desresp.code = resp.code
        desresp.msg = resp.msg
        desresp.other = peer.user_id
        desresp.callback = resp.callback
        self.sendOne(desPeer, desresp)

    def onRefresh(self, timestamp):
        """ 刷新 """
        super(CommonServer, self).onRefresh(timestamp)
        if timestamp - self.lastCheckCommandsTimes > COMMANDS_TICK_TIME:
            # print("[onRefresh] %s, %s" % (timestamp, self.lastCheckCommandsTimes))
            data = self.channel.parse_response(block=False, timeout=1)
            if data:
                try:
                    cType, cMsg, cCommands = tuple(data)
                    if cType != "subscribe":
                        rType, rCommands, rOther = tuple(cCommands.split("|"))
                        if rCommands == "X0_CC_00_XX_PP_CLOSE":
                            print("收到关服信息")
                            self.isConnect = False
                            for _player in self.peerList:
                                _player.dropConnection('服务器即将进行维护.')
                            # 开始关闭服务器
                            from twisted.internet import reactor
                            reactor.stop()
                        elif rCommands == "X0_CC_02_XX_PP_INTEFACE":
                            print("收到接口更新通知 %s, %s" % (rType, rOther))
                            user_ids = [int(i) for i in rOther.split(",")]
                            resp = impb.S_C_infor()
                            resp.code = str(int(rType))
                            resp.msg = u'接口更新'
                            resp.other = rOther
                            resp.callback = rCommands
                            peers = []
                            for _iter in user_ids:
                                if self.userPeers.get(_iter):
                                    peers.append(self.userPeers.get(_iter))
                            print('response inteface: %s' % resp)
                            if peers:
                                self.send(peers, resp)
                        elif rCommands == 'X0_CC_02_XX_PP_NOTICE':
                            print('收到通知信息: %s, %s, %s' % (rType, rCommands, rOther))
                            newOther = json.loads(rOther)
                            user_ids = [int(i) for i in newOther["user_ids"]]
                            resp = impb.S_C_infor()
                            resp.code = str(int(rType))
                            resp.msg = u'通知消息'
                            resp.other = repr(newOther)
                            resp.callback = rCommands
                            peers = []
                            notPeers = []
                            print('response notece: %s' % resp)
                            for _iter in user_ids:
                                if self.userPeers.get(_iter):
                                    peers.append(self.userPeers.get(_iter))
                                else:
                                    notPeers.append(_iter)

                            if peers:
                                self.send(peers, resp)

                            if resp.code == 9:
                                respMsg = impb.S_C_Send_msg()
                                respMsg.user_id = str(newOther["inviter"])
                                respMsg.type = 7
                                # respMsg.state = 2
                                respMsg.target_group_id = newOther["group_ids"].replace('g', '')
                                respMsg.Message.content = "群聊被解散"
                                data = respMsg.SerializeToString()
                                for _iter in notPeers:
                                    redis.lpush("message:pool:%s" % _iter, data)
                                self.send(peers, respMsg)

                except Exception as err:
                    traceback.print_exc()
                    print(err)
            self.lastCheckCommandsTimes = timestamp
