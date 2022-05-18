
from im.common.pack  import *
# from im.common.proto import msg_interface_pb2 as interface_pb2
from im.common.proto import im_pb2 as impb
from im.common.server import Server

class CommonRegister(Server):
    """ 协议注册类 """

    def __init__(self, *args, **kwargs):
        super(CommonRegister, self).__init__(*args, **kwargs)

    def registerProtocolResolver(self):
        unpacker = Unpacker
        self.recverMgr.registerCommands(( \
            unpacker(impb.C_S_PING, impb.C_S_Ping, self.onPing), \
            unpacker(impb.C_S_SEND, impb.C_S_Send_msg, self.onSend), \
            unpacker(impb.C_S_INFOR, impb.C_S_infor, self.onInfo), \
            ))
        packer = Packer
        self.senderMgr.registerCommands(( \
            packer(impb.S_C_PING, impb.S_C_Ping), \
            packer(impb.S_C_ERROR, impb.S_C_error), \
            packer(impb.S_C_INFOR, impb.S_C_infor), \
            packer(impb.S_C_SEND, impb.S_C_Send_msg), \
            packer(impb.S_C_SEND_INFO, impb.S_C_Send_Info), \
            packer(impb.S_C_ONLINE, impb.S_C_Online), \
            packer(impb.S_C_ADD_ONLINE, impb.S_C_Add_Online), \
            packer(impb.S_C_SIGN_OUT, impb.S_C_Sign_Out), \
            packer(impb.S_C_OFFLINE_MESSAGE, impb.S_C_Offline_Message), \
        ))