#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved
import time
from configs import *
from status.exceptions import *

class mysqlOperation(object):

    db = None

    @classmethod
    def beforConnect(cls, *args, **kwargs):
        """ 数据库连接前操作

        :param args:
        :param kwargs:
        :return:
        """
        print("[beforConnect] %s, %s" %(args, kwargs))
        return True, {}

    @classmethod
    def afterConnect(cls, response):
        """ 数据库连接后操作

        :param args:
        :param kwargs:
        :return:
        """
        print("[afterConnect] [args: %s]" % (response))
        cls.db = response["response_func"]
        if RUNNING != 'api':
            cls.generateServer()
        return response["response_func"]

    @classmethod
    def generateServer(cls):
        """ 初始化服务器信息

        :return:
        """
        pass

    @classmethod
    def gameStart(cls, **options):
        """ 启动服务 """
        # cls.update("server", where=("server_code='%s'" % SERVER_CODE, {}), data={"status": 1})
        pass

    @classmethod
    def gameStop(cls, **options):
        """ 关闭服务 """
        #cls.update("server", where=("server_code='%s'" % SERVER_CODE, {}), data={"status": 0})
        pass

    @classmethod
    def generateInertSql(cls, table, data):
        """ 生成SQL语句

        :param table:
        :param data:
        :return:
        """
        reprs = str(tuple(i for i in data.keys())).replace(",)", ")").replace("'", '`').replace('"', '`')
        value = str(tuple(":%s" % i for i in data.keys())).replace(",)", ")").replace("'", '').replace('"', '')
        sql = "INSERT INTO %(table)s %(reprs)s VALUES %(value)s" % {"table": table, "reprs": reprs, "value": value}
        return sql

    @classmethod
    def generateUpdateSql(cls, table, where=(), data={}):
        """更新数据设置
        :parmas where:
             where[0] = ":is_deleted=:is_deleted or `status` in (SELECT x FROM Y WHERE I =:i )"
             where[1] = {"is_deleted": 0, "i": 2}
        :params data:

            {
                "key": "value"

            }
        """
        upr = ",".join(["%s=:%s" % (i, i) for i in data])

        update = "UPDATE %(table)s SET %(upr)s %(where)s" % {"table": table, "upr": upr,
                                                             "where": " where " + where[0] if where[0] else ""}

        # 检查条件
        data.update(where[1])

        return update

    @classmethod
    def insert(cls, table, data):
        """ 插入数据

        :param table: 表名称
        :param data:  数据内容
        :return: 返回插入数据的ID
        """
        try:
            sql = cls.generateInertSql(table, data)
            data_id = cls.db.insert(sql, data)
            return data_id
        except Exception as err:
            print(sql)
            print(err)

    @classmethod
    def update(cls, table, where=(), data={}):

        sql = cls.generateUpdateSql(table, where, data)
        return cls.db.update(sql, data)

    @classmethod
    def delete(cls, table, where, **kwargs):

        pass