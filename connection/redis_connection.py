#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved
import redis

from control import redisOperation
from modules import Event
from .default_connection import DefaultConnect




class RedisConnect(DefaultConnect):
    """ 获取REDIS配置
    """
    @Event.after(redisOperation.afterConnect)
    @Event.befor(redisOperation.beforConnect)
    def connection(self, *args, **kwargs):
        """ 创建连接
        """
        redisdb = redis.ConnectionPool(host=self.configs.host,
                                       port=self.configs.port,
                                       db=self.configs.database,
                                       password=self.configs.password,
                                       decode_responses= True)
        return redis.Redis(connection_pool=redisdb)

    @staticmethod
    def extendsConnection(**ConnectConfigs):
        otherRedis = redis.ConnectionPool(**ConnectConfigs, decode_responses=True)
        return redis.Redis(connection_pool=otherRedis)

    def __str__(self):
        return "[RedisConnect][ip] %s, [port] %s, [db] %s" % (self.configs.host, self.configs.port, self.configs.database)


