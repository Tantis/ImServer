#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved

# 定义异常错误信息
class SystemException(Exception):
    """ 系统错误

    """
    pass

class LoginException(Exception):
    """ 用户登陆出错

    """
    pass