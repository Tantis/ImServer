#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved

from .code import UserResponse, SystemResponse, RoleResponse, ImageResponse, VersionResponse, DefaultStateCode

def resultCode(response, data={}, tree=[]):
    """ 返回函数 """
    # import ipdb
    # ipdb.set_trace()

    # code, msg = response.iteritems().next()
    code, msg = next(iter(response.items()))
    result = {"code": code, "msg": msg}
    if data:
        result.update({"data": data})
    if tree:
        result.update({"list": tree})
    return result