from websocket import create_connection
from im.common.proto import im_pb2 as impb
import time
from im.common.pack import *
senderMgr = SendManager()
recverMgr = RecvManager()
def Ping(*args, **kwargs):
    print(args, kwargs)

def recvMsg(player, resp):
    print(resp)

senderMgr.registerCommands(( \
    Packer(impb.C_S_PING, impb.C_S_Ping),
    Packer(impb.C_S_SEND, impb.C_S_Send_msg),
))
recverMgr.registerCommands((\
    Unpacker(impb.S_C_Ping, impb.S_C_Ping, Ping),
    Unpacker(impb.S_C_SEND, impb.S_C_Send_msg, recvMsg),
    Unpacker(impb.S_C_ERROR, impb.S_C_error, recvMsg),
    Unpacker(impb.S_C_SEND_INFO, impb.S_C_Send_Info, recvMsg),
    Unpacker(impb.S_C_ONLINE, impb.S_C_Online, recvMsg),
    Unpacker(impb.S_C_ADD_ONLINE, impb.S_C_Add_Online, recvMsg),
    Unpacker(impb.S_C_SIGN_OUT, impb.S_C_Sign_Out, recvMsg),
    Unpacker(impb.S_C_OFFLINE_MESSAGE, impb.S_C_Offline_Message, recvMsg),

))

# ws = create_connection("ws://127.0.0.1:5056"
#                        )
ws = create_connection("ws://127.0.0.1:18080", header={"token": 'b149d84d85d79eea6bfdfd1b63872da2'})
resp = impb.C_S_Send_msg()
resp.msg_id = "12346"
resp.session_id = 'imid_tqczivyg9u86'
resp.client_msg_id = '123456'
resp.user_id = 52
resp.group_id = 0
resp.type = 1
resp.Message.content = b'123456'
resp.Message.image_url = '123456'

ws.send_binary(senderMgr.pack(resp))
while True:
    data = ws.recv()
    print(data)
    print(recverMgr.unpackCall(0, data))
    # break
ws.close()