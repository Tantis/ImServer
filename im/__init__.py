import configs
from connection import RedisConnect
from connection import MysqlConnect

conf   = RedisConnect(configs.REDIS_CONFIG["host"],
                      configs.REDIS_CONFIG["port"],
                      '', configs.REDIS_CONFIG["password"],
                      configs.REDIS_CONFIG["db"])

myConf = MysqlConnect(configs.READS_MYSQL_CONFIG["host"],
                      configs.READS_MYSQL_CONFIG["port"],
                      configs.READS_MYSQL_CONFIG["user"],
                      configs.READS_MYSQL_CONFIG["password"],
                      configs.READS_MYSQL_CONFIG["db"]
                      )
redis = conf.conn
mysql = myConf.conn


# from generate.generateConfigs import GenerateConf
# data  = GenerateConf()


