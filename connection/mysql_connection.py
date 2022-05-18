
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved
import copy
from driver.db import MySQLdb

from .default_connection import DefaultConnect
from control import mysqlOperation
from modules import Event

class MysqlConnect(DefaultConnect):

    @Event.after(mysqlOperation.afterConnect)
    @Event.befor(mysqlOperation.beforConnect)
    def connection(self, *args, **kwargs):
        """
        :params args: 
        """    
        configs = copy.copy(self.configs)
        del configs["kwargs"]
        return MySQLdb(configs)

    def __str__(self):
        
        return "[MysqlConnect][ip] %s, [port] %s, [db] %s" % (self.configs.host, self.configs.port, self.configs.database)






