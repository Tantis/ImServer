# -*- coding: utf-8 -*-
import traceback
from im.common.proto import msg_interface_pb2 as interface_pb2
from struct import pack, unpack
from twisted.internet.protocol import Protocol
import struct
import gzip
from autobahn.twisted.websocket import WebSocketServerProtocol

from .log import Logger as logger
import asyncio
from io import StringIO

KICK_OUT_TICK = 2 * 60 * 60 * 1000
PACKET_TICK_LIMIT = 200
PACKET_COUNT_LIMIT = 18
MAX_INVALID_COUNT = 300
DROP_TICK = 15000
PEER_TIME_TACK = 5 * 1000
PING_INTERVAL_TICK = 15*1000

# 编码、解码器
class Peer(WebSocketServerProtocol, object):
    """

    """
    def __init__(self):
        super(Peer, self).__init__()
        self.number = 0
        self.map = []
        self.controlPlayer = self
        self.reset()

    def reset(self):
        """
        Reset peer data
        """
        self.hashKey = None
        self.descTxt = None
        self.protoTag = None
        self.ip = None
        self.port = None
        self.isConnected = False
        self.lastPacketTimestamp = 0
        self.lastPingTime = 0
        self.dropedTimestamp = 0
        self.firstPacketTimestamp = 0
        self.firstPacketClientTimestamp = 0
        self.packetClientTimestamps = []
        self.invalidCount = 0
        self.payload = {}
        self.device_number = ''
        self.user_id = 0
        self.accessToken = ''

    def onOpen(self):
        super(Peer, self).onOpen()
        # self.factory.peerList.append(self)
        if self.hashKey:
            # print(u'client[%s] handshake finished.'%(self.descTxt))
            print("协议头:%s" % self.websocket_protocols)
            # self.websocket_protocols = self.token
            self.factory.addPeer(self)
            self.isConnected = True
            self.lastPacketTimestamp = self.factory.getTimestamp()
            print(u"连接成功:%s" % self.user_id)

    def onConnect(self, request):
        print("[onConnect] %s: %s" % (request.origin, request))
        super(Peer, self).onConnect(request)
        self.token = request.headers.get('token') or request.headers.get("sec-websocket-protocol")
        self.hashKey = str(hash(request.peer))
        self.descTxt = str(request.peer)

        print(u'client[%s] hash[%s] try connecting.'%(self.descTxt, self.hashKey))
        custom_header = {}
        # if request.headers['sec-websocket-protocol']:
        if request.headers.get("sec-websocket-protocol"):
            custom_header['sec-websocket-protocol'] = self.token
            return (None, custom_header)

    def onMessage(self, payload, isBinary):
        print("onMessge:%s" % payload)
        isValidTimestamp = False
        try:
            self.factory.resolveMsg(self, payload)
        except Exception as e:
            traceback.print_exc()
            self.invalidCounter('Received or Resolved packet error[%s]'%(e))
            return

    def drop(self, reason, reasonCode):
        self.dropedTimestamp = self.factory.getTimestamp() + DROP_TICK

    def isTimeout(self, timestamp):
        return timestamp - self.lastPacketTimestamp > KICK_OUT_TICK

    async def onCheck(self, timestamp):

        # print("onCheck[%s]peer[%s]clientIP[%s] " % (timestamp, self.hashKey, self.client_ip))
        # if  self.isTimeout(timestamp):
        #     self.lastPacketTimestamp = timestamp
        #     return False
        # if self.dropedTimestamp and timestamp > self.dropedTimestamp:
        #     self.dropConnection(False)
        #     self.factory.removePeer(self)
        #     self.reset()
        #     return False
        return True

    def checkPacketTimestamp(self, clientTimestamp):
        if self.firstPacketTimestamp:
            deltaTime = clientTimestamp - self.firstPacketClientTimestamp
            idx = 0
            for i in range(len(self.packetClientTimestamps) - 1, -1, -1):
                if clientTimestamp - self.packetClientTimestamps[i] > PACKET_TICK_LIMIT:
                    idx = i + 1
                    break
            del self.packetClientTimestamps[:idx]
            # log('packetClientTimestamps[%s]'%(self.packetClientTimestamps))
            return len(self.packetClientTimestamps) < PACKET_COUNT_LIMIT
        return True

    def invalidCounter(self, reason):
        self.invalidCount += 1
        if self.invalidCount >= MAX_INVALID_COUNT:
            self.drop('Too many invalid count.', 400)

    def dropConnection(self, abort):
        super(Peer, self).dropConnection(abort=abort)

    def onClose(self, wasClean, code, reason):
        print("%s, %s, %s" % (wasClean, code, reason))
        super(Peer, self).onClose(wasClean, code, reason)
        if self.isConnected:
            print(u'client[%s] disconnected reason[%s]'%(self.descTxt, reason))
            self.factory.removePeer(self)
            self.reset()
        else:
            print(u'client[%s] disconnected error:no found descTxt'%(self.descTxt))

    def onSkipViolationProtocol(self):
        #self.onMessage(self.data, self.message_is_binary)
        self.data = b''

    def GetFriends(self):

        return []

    def GetGroups(self, group_id):

        return []
