#
# from im.common.proto import im_pb2 as impb
# import time
# from im.common.pack import *
# senderMgr = SendManager()
# recverMgr = RecvManager()
# def Ping(*args, **kwargs):
#     print(args, kwargs)
#
# def recvMsg(player, resp):
#     print(resp)
# b = "\n\x03363\x12\x12imid_dtoszbh9wg117\x1a\x0252*\x031842\x010=\x01\x00\x00\x00B\t181695823M\x01\x00\x00\x00R)\n\x06432432\"\x132019-12-08 17:19:10*\n1575796750"
#
# sc = impb.S_C_Send_msg()
# sc.ParseFromString(b.encode('utf8'))
# print(sc)
#
#
#
import schedule

import time
number = {}
# 定义你要周期运行的函数
def job(id):
    number.setdefault(id, 0)
    number[id] += 1
    print("I'm working...")
    if number[id] >= 3:
        return schedule.CancelJob
        number[id] = 0

schedule.every(1).seconds.do(job, id=5)
while True:
    schedule.run_pending()  # 运行所有可以运行的任务

    # time.sleep(1)