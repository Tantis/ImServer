from connection.redis_connection import RedisConnect
from configs import OTHER_CONFIG
from im.db_define import CHANNEL_COMMANDS

if __name__ == "__main__":
    redis = RedisConnect.extendsConnection(**OTHER_CONFIG)
    redis.publish(CHANNEL_COMMANDS, "0|X0_CC_00_XX_PP_CLOSE|123")
