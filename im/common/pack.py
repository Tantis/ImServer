import struct, gzip
from io import StringIO
from .log import *
import traceback

class Packer(object):
    def __init__(self, msg_code, msg_cls, compress=False, timestamp=False):
        self.msg_code = msg_code
        self.msg_cls = msg_cls
        self.compress = compress
        self.timestamp = timestamp

    def pack(self, protocol_object):
        assert isinstance(protocol_object, self.msg_cls)
        # print(self.msg_code)
        print('protocol_object: %s' % protocol_object)
        _data = struct.pack('>I', self.msg_code) + protocol_object.SerializeToString()
        print('pack---source: %s' % _data)
        _data = b"%s" % _data
        # _data = _data.decode('utf8', 'ignore').encode('utf8')
        print("pack:%s" % _data)
        # if self.compress:
        #     mstream = StringIO()
        #     f = gzip.GzipFile(mode='wb', compresslevel=6, fileobj=mstream)
        #     f.write(_data)
        #     f.close()
        #     _data = mstream.getvalue()
        #     mstream.close()
        # if self.timestamp:
        #     insertData = chr(self.compress) + chr(self.timestamp) + struct.pack('>Q', int(time.time()*1000))
        # else:
        #     insertData = chr(self.compress) + chr(self.timestamp)
        #insertData = ''
        #compressIdx = int((len(_data) + len(insertData))/3)
        #print("%s, %s, %s, %s"%(_data, compressIdx, insertData, compressIdx))
        #_data = _data[:compressIdx] + insertData.encode("utf8") + _data[compressIdx:]
        #_data = _data.encode("utf8")
        return _data
        #return _data

class Unpacker(object):
    def __init__(self, msg_code, msg_cls, callback):
        assert callable(callback), "resolver[%s] is not a callable object"%(str(callback))
        self.msg_code = msg_code
        self.msg_cls = msg_cls
        self.callback = callback

    def unpack(self, data):
        obj = self.msg_cls()
        print("[obj] %s" % obj)
        obj.ParseFromString(data)
        return obj

class SendManager(object):
    def __init__(self):
        self._cmds = {}

    def registerComand(self, cmd_inst):
        assert isinstance(cmd_inst, Packer) \
            and (cmd_inst.msg_cls.__name__ not in self._cmds)
        self._cmds[cmd_inst.msg_cls.__name__] = cmd_inst

    def registerCommands(self, commands):
        for cmd_inst in commands:
            self.registerComand(cmd_inst)

    def pack(self, protocol_object):

        assert protocol_object.__class__.__name__ in self._cmds
        msg_name = protocol_object.__class__.__name__
        # print(msg_name)
        cmd_inst = self._cmds[msg_name]
        print(u'Send pack [%s]'%(msg_name))
        msg = cmd_inst.pack(protocol_object)
        return msg

    def hasCmd(self, msg_name):
        return self._cmds.has_key(msg_name)

class RecvManager(object):
    def __init__(self):
        self._cmds = {}

    def registerCommand(self, cmd_inst):
        assert(isinstance(cmd_inst, Unpacker) \
            and (cmd_inst.msg_code not in self._cmds))

        self._cmds[cmd_inst.msg_code] = cmd_inst

    def registerCommands(self, commands):
        for cmd_inst in commands:
            self.registerCommand(cmd_inst)

    def unpackCall(self, arole, msg):

        try:
            print(msg)
            msg_code, = struct.unpack('>I', msg[:4])
            print("recv %s, %s" % ( msg_code, self._cmds[msg_code]))
            if msg_code not in self._cmds:
                raise Exception('msg_code[%s] is not existed.'%(msg_code))
            cmd_inst = self._cmds[msg_code]
            proto_obj = cmd_inst.unpack(msg[4:])
        except Exception as e:
            traceback.print_exc()
            return False

        # if arole:
        #     log(u'try unpack [%s] from [%s]'% \
        #         (cmd_inst.msg_cls, arole.descTxt), LOG_LEVEL_RELEASE)
        # else:
        #     log(u'try unpack [%s]'%cmd_inst.msg_cls, LOG_LEVEL_RELEASE)

        # log(u'unpacked [%s] [%s]'%(cmd_inst.msg_cls, proto_obj))

        params = [proto_obj]
        if arole is not None:
            params.insert(0, arole)
        cmd_inst.callback(*params)
        return cmd_inst.msg_code, cmd_inst.callback, params

    def clientUnpackCall(self, msg):
        return self.unpackCall(None, msg)

    def hasCmd(self, msg_header):
        return self._cmds.has_key(msg_header)
