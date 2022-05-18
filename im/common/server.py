#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import traceback
import schedule
from autobahn.twisted.websocket import WebSocketServerFactory
from twisted.internet.task import LoopingCall
import asyncio

from im.player import TcpServerHandle
from im.common.pack import *
from im.common.peer import  Peer
from .log import Logger as logger

CHECK_PEER_TICK = 5000
TICK_PEERS_COUNT = 10
MAX_PACKET_PER_TICK = 100

GROUP_TIME_CHECK = 5000

class Server(WebSocketServerFactory):
    """ 基础连接类 """
    protocol = TcpServerHandle

    def __init__(self, *args, **kwargs):
        # super(Server, self).__init__(*args, **kwargs)
        super(Server, self).__init__()
        self.peers = {}
        self.tokenPeers = {}
        self.userPeers = {}
        self.peerList = []
        self.tickPeerIdx = 0
        self.initNetManager()
        self.tickTimer = LoopingCall(self.onTick)
        self.tickTimer.start(0.5, False)
        self.lastCheckTimestamp = self.getTimestamp()
        self.lastCheckGroupTimestamp = self.getTimestamp()
        self.msgBuffers = []

    def getTimestamp(self):
        return int(time.time()*1000)

    def logPrefix(self):
        """
        Describe this factory for log messages.
        """
        return self.__class__.__name__

    def sendData(self, peer, data):
        if not peer:
            print("用户连接已经关闭")
            return
        print("给目标用户发送PROTOBUF： %s-%s" % (peer.user_id, len(data)))
        peer.sendMessage(data, True)

    def sendOne(self, peer, protocol_obj):
        assert isinstance(peer, Peer)
        print("[发送单个用户数据] 用户：%s 数据：%s" % (peer, protocol_obj))

        self.sendData(peer, self.senderMgr.pack(protocol_obj))

    def send(self, peers, protocol_obj, excludes=()):
        data = self.senderMgr.pack(protocol_obj)
        # print(self.recverMgr.unpackCall(0, data))
        for peer in peers:
            if peer not in excludes:
                self.sendData(peer, data)

    def sendAll(self, protocol_obj):
        self.send(self.peerList, protocol_obj)

    def getResolverMgr(self):
        return self.senderMgr, self.recverMgr

    def initNetManager(self):
        self.senderMgr = SendManager()
        self.recverMgr = RecvManager()
        self.registerProtocolResolver()

    def registerProtocolResolver(self):
        raise 'abstract interface'

    def onAddPeer(self, peer):
        pass

    def onRemovePeer(self, peer):
        pass

    def addPeer(self, peer):
        assert peer.hashKey not in self.peers, "Peer[%s] is existed."%(peer.descTxt)
        self.peers[peer.hashKey] = peer
        self.tokenPeers[peer.token] = peer
        self.userPeers[peer.user_id] = peer
        self.onAddPeer(peer)
        self.peerList.append(peer)
        # print(self.peers)
        print("当前增加用户：%s" % peer)

    def removePeer(self, peer):
        if peer.hashKey not in self.peers:
            print("Peer[%s] is not existed."%(peer.descTxt))
            return
        del self.peers[peer.hashKey]
        if peer.token not in self.tokenPeers:
            print("Peer[%s] is not existed." % (peer.token))
            return
        del self.tokenPeers[peer.token]
        if peer.user_id not in self.userPeers:
            print("Peer[%s] is not existed." % (peer.user_id))
            return
        if peer in self.peerList:
            self.peerList.remove(peer)
        del self.userPeers[peer.user_id]

        self.onRemovePeer(peer)


    def isValidPacket(self, msgName):
        # raise 'abstract interface'
        print(msgName)

    def onTick(self):
        # print("11111111111")
        timestamp = self.getTimestamp()
        try:
            self.onRefresh(timestamp)
        except:
            for tb in traceback.format_exc().splitlines():
                # logger.error(tb)
                print(tb)

    def addUserPeers(self, user_id, peer):
        # assert user_id not in self.userPeers, "Peer[%s] is existed." % (user_id)
        self.userPeers[user_id] = peer

    async def checkPlayer(self, peers, timestamp):

        tasks = []
        for peer in peers:
            # peer.onCheck(timestamp)
            task = asyncio.create_task(peer.onCheck(timestamp))
            print(task)
            tasks.append(task)
        asyncio.gather(*tasks, return_exceptions=True)

    def onCheck(self, timestamp):

        self.lastCheckTimestamp = timestamp
        countPeers = len(self.peerList)
        if countPeers <= 0:
            return

        if self.tickPeerIdx >= countPeers:
            self.tickPeerIdx = 0

        peers = self.peerList[self.tickPeerIdx:self.tickPeerIdx+TICK_PEERS_COUNT]
        self.tickPeerIdx += TICK_PEERS_COUNT

        # 异步运行玩家检测
        print('开始异步检查')
        asyncio.run(self.checkPlayer(peers, timestamp))
        print('OnCheck 运行结束')

    def onCheckGroupTimer(self, timestramp):

        pass

    def onRefresh(self, timestamp):
        # print("onRefresh: %s" % timestamp)
        if timestamp - self.lastCheckTimestamp > CHECK_PEER_TICK:
            #self.onCheck(timestamp)
            pass
        if timestamp - self.lastCheckGroupTimestamp > GROUP_TIME_CHECK:
            self.lastCheckGroupTimestamp = timestamp
            self.onCheckGroupTimer(timestamp)
        schedule.run_pending()

    def recvPacket(self, peer, buf):
        self.msgBuffers.append((peer, buf))

    def resolveMsg(self, peer, msgData):
        # print(peer, msgData)
        recvMgr = self.recverMgr
        unpackRes = recvMgr.unpackCall(peer, msgData)
        # print("unPackres: %s" % unpackRes)
        if not unpackRes:
            peer.invalidCounter('Invalid data for resolved.')
        elif self.isValidPacket(unpackRes[0]):
            peer.lastPacketTimestamp = self.getTimestamp()

    def resolvePacket(self, timestamp):
        recvMgr = self.recverMgr
        #log(u'Packet count[%d]'%(len(self.msgBuffers)))
        for peer, packet in self.msgBuffers[:MAX_PACKET_PER_TICK]:
            unpackRes = recvMgr.unpackCall(peer, packet)
            if not unpackRes:
                peer.invalidCounter('Invalid data for resolved.')
            elif self.isValidPacket(unpackRes[0]):
                peer.lastPacketTimestamp = timestamp
        self.msgBuffers = self.msgBuffers[MAX_PACKET_PER_TICK:]

    def resolvePacketOnPeerClose(self, peer):
        recvMgr = self.recverMgr
        for buf in self.msgBuffers[:]:
            if buf[0] == peer:
                recvMgr.unpackCall(buf[0], buf[1])
                self.msgBuffers.remove(buf)
