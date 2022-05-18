#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved

import time

SERVER_CODE   = "DMGY_SERVER"
SERVER_NAME  = "大漠孤烟"
SERVER_ID    = 1
SERVER_VERSION = "0.1.2"
LISTEN_PORT    = 18080
LISTEN_IP      = '106.13.4.228'
RUNNING        = "server" # 运行的服务 server=游戏服务 api=接口服务


# 推送服务器配置
Jpush_AppKey = "8cc9b695c1ba72204f02b1c3"
Jpush_Secret = "8d1dac8f7d6bcc6ac1f8cf66"

REDIS_CONFIG = {"host": '106.13.4.228',"port": 6379, "password": "Aa6618", "db": 5}  # 主REDIS服务
OTHER_CONFIG = {"host": '106.13.4.228',"port": 6379, "password": "Aa6618", "db": 8}  # 订阅的REDIS

# 数据库配置
WRITE_MYSQL_CONFIG = {"host": 'lyproject.top',"port": 3306, "user": "user", "password": "Einiter", "db": "im_server"}
READS_MYSQL_CONFIG = {"host": 'lyproject.top',"port": 3306, "user": "user", "password": "Einiter", "db": "im_server"}

LOGGER_CONFIG =  {
        "version": 1,
        "formatters": {
            "format_def": {
                "class": "logging.Formatter",
                "format": "%(asctime)s:[%(levelname)s][%(module)s][%(name)s.%(funcName)s][%(filename)s:%(lineno)d]%(message)s ",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "format_def"
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "format_def",
                "filename": "log/api_server_%s.log" % time.strftime("%Y-%m-%d", time.localtime()),
                "mode": "a",
                "maxBytes": 50 * 1024 * 1024,
                "backupCount": 5
            }
        },
        "loggers": {
            "api_server": {
                "level": "INFO",
                "propagate": 0,
                "handlers": [
                    "file", "console"
                ]
            },
            "game_server": {
                "level": "INFO",
                "propagate": 0,
                "handlers": [
                    "file", "console"
                ]
            }
        }
    }
