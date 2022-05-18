# -*- coding: utf-8 -*-

import random

from im import redis
from im.common.log import Logger as logger
from im.common.peer import Peer
from im.common.proto import im_pb2 as impb
from configs import SERVER_CODE
from im.db_define import  *
import time


PING_INTERVAL_TICK = 15*1000

# 逻辑代码
class TcpServerHandle(Peer):

    def __init__(self):
        super(TcpServerHandle, self).__init__()
        self.role = None
        self.token = None
        self.user_id = None
        self.refresh_increase = 0

    def onOpen(self):
        #  检查用户TOKEN信息
        print("[onOpen]: user:%s" % self.token)
        if not self.token:
            self.dropConnection('TOKEN不能为空')
            return

        token = self.token
        if redis.exists("user:token:%s" % token) and redis.type("user:token:%s" % token) == 'hash':
            user_id = redis.hget("user:token:%s" % token, "user_id")
            self.user_id = int(user_id)
        else:
            self.codeErrorMsg(403, 'TOKEN不存在,无法连接')
            self.dropConnection('TOKEN 不存在')
            return

        if not self.user_id:
            self.codeErrorMsg(403, '用户ID不存在,无法连接')
            self.dropConnection('用户ID不存在')
            return
        if self.factory.userPeers.get(user_id):
            peer = self.factory.userPeers[user_id]
            peer.codeErrorMsg(401, '当前用户已经被其他用户登录，请重新登录')
            peer.dropConnection('用户被占用')
        print('onOpen: user_id:%s token:%s' % (self.user_id, self.token))
        super(TcpServerHandle, self).onOpen()

    def codeErrorMsg(self, code, msg):
        """ 发送错误信息 """
        resp = impb.S_C_error()
        resp.code = code
        resp.msg = msg
        self.factory.sendOne(self, resp)
        return

    def OnRefresh(self):
        """ 收到PING包后的数据刷新策略 """
        if self.refresh_increase >= 5000:
            self.refresh_increase = 0
        self.refresh_increase += 1

        # 判断TOKEN 是否存在
        if self.token:
            if not redis.exists("user:token:%s" % self.token):
                self.dropConnection('TOKEN 已经过期')


    async def onCheck(self, timestamp):
        # print("peer onCheck %s" % timestamp)
        # if timestamp - self.lastPacketTimestamp > PING_INTERVAL_TICK:
        #     self.isOnline = False
        if timestamp - self.lastPingTime >= PING_INTERVAL_TICK:
            self.factory.onPing()
            self.lastPingTime = timestamp
        await super(TcpServerHandle, self).onCheck(timestamp)

        # print("peer onCheck %s" % 'result')

    def GetFriends(self):
        """ 获取好友列表 """
        user_ids = list(redis.smembers(USER_FRIENDS_SET % {"user_id": self.user_id}))
        print("[GetFriends]%s" % user_ids)
        return [int(i) for i in user_ids]

    def GetGroups(self, group_id):
        """ 获取组内用户 """
        user_ids = list(redis.smembers(USER_GROUPS_SET % {"group_id": group_id}))
        print("[GetGroupsUsers]%s" % user_ids)
        return [int(i) for i in user_ids]

    def GetJoinGroups(self, group_id):
        """ 判断是否属于当前组内用户 """
        if self.user_id in self.GetGroups(group_id):
            return True
        return False

    def send(self, user_id, group_id, msg_type, resp):
        """ 发送用户或者群组消息 """
        msgResponse = impb.S_C_Send_msg()
        client_msg_id = resp.client_msg_id
        msgResponse.msg_id = resp.msg_id
        # 不存在消息ID不发送任何信息直接返回
        if not resp.msg_id:
            return
        if not resp.session_id:
            er = impb.S_C_Send_Info()
            er.msg_id = resp.msg_id
            er.state = -1
            er.client_msg_id = resp.client_msg_id
            er.content = u'没有会话ID'
            print(resp.user_id, er.content)
            self.factory.sendOne(self, er)
            return

        msgResponse.target_group_id = str(group_id)
        msgResponse.type = msg_type
        msgResponse.client_msg_id = resp.client_msg_id
        msgResponse.user_id = str(self.user_id)
        msgResponse.target_user_id = str(user_id)
        msgResponse.session_id = resp.session_id
        content = resp.Message.content
        msgResponse.Message.content = content
        if msg_type == 1:
            print(content)
            msgResponse.Message.content = content
        elif msg_type == 2:
            msgResponse.Message.image_url = resp.Message.image_url
        elif msg_type == 3:
            msgResponse.Message.file_url = resp.Message.file_url
        else:
            msgResponse.Message.content = resp.Message.content
        msgResponse.Message.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        msgResponse.Message.timestamp = str(int(time.time()))
        if group_id > 0:
            self.factory.sendGroupMsg(self, group_id, msgResponse)
            return
        self.factory.sendMsg(self, user_id, msgResponse)
