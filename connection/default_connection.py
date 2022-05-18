#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved

from modules import model
from modules import Event
"""

        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "qwe",
        "maxConnections": 55,
        "minFreeConnections": 11,

"""

class operation(object):

    @classmethod
    def afterConnection(cls, *args, **kwargs):
        print("[afterConnection] %s, %s" % (args, kwargs))


class DefaultConnect(object): 
    
    def __init__(self, ip, port, user, password, db, **kwargs):
        
        self.configs = model()
        self.configs.host = ip
        self.configs.port = port
        self.configs.user = user
        self.configs.password = password
        self.configs.kwargs = model(kwargs)
        self.configs.database = db
        self.configs.maxConnections = 55
        self.configs.minFreeConnections = 11
        self.conn = self.connection()


    @Event.after(operation.afterConnection)
    def connection(self, *args, **kwargs):
        """ 创建连接
        
        """
        
        pass
    
    def sets(self, table, value, type=0, **kwargs):
        """ 修改数据

        """
        pass 
    
    
    def adds(self, table, value, type=0, **kwargs):
        """ 新增数据

        """
        pass

    def dels(self, table, value, type=0, **kwargs):
        """删除数据

        """
        pass


