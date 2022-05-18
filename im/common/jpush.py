import jpush
from configs import Jpush_AppKey, Jpush_Secret

class JpushControl(object):

    @classmethod
    def createPush(cls, *args, **kwargs):
        conn = jpush.JPush(Jpush_AppKey, Jpush_Secret)
        push = conn.create_push()
        cls.push = push
        return push

    @classmethod
    def send(cls, platform, register_ids, content, extras):
        """ 发送通过register_id推送信息 """
        try:
            _push = cls.createPush()
            _push.platform = jpush.all_ # jpush.platform(*platform)
            _push.audience = jpush.registration_id(*tuple(register_ids))  #jpush.audience("registration_id", jpush.registration_id(register_ids))
            # {"registration_id": jpush.registration_id(register_ids)}
            # _push.notification =  jpush.notification(alert=content)
            _push.message = jpush.message(content, extras=extras)
            _push.send()
        except Exception as err:
            print(err)








