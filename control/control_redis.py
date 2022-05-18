#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved


class redisOperation(object):
    redis = None
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
        cls.redis = response["response_func"]
        return response["response_func"]

    @classmethod
    def query(cls, *args, **kwargs):
        pass

