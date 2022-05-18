#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved


class DefaultStateCode:
    SUCCESS = {"status": 200, "msg": "成功"}
    ERROR = {"status": 400, "msg": "失败"}
    ARGS_CODE_ERROR_01 = {"status": 400, "msg": "輸入的驗證碼不正確、或者沒有輸入"}
    ARGS_ARGS_ERROR_01 = {"status": 400, "msg": "没有输入账号信息"}
    ARGS_ARGS_ERROR_02 = {"status": 400, "msg": "没有输入密码信息"}
    ARGS_ERROR_01 = {"status": 401, "msg": "验证码输入错误"}
    ARGS_ERROR_02 = {"status": 401, "msg": "用户不存在，或者电话号码与账号有误"}
    ARGS_ERROR_03 = {"status": 401, "msg": "请输入账号"}


# 定义基础错误信息
SYSTEM_RESPONSE = dict(
    TOKEN_ERROR         = {401: u'没有传递TOKEN信息'},
    TOKEN_EXISTS_ERROR  = {402: u'TOKEN信息不存在或者已过期'},
    ACCESS_RULE_ERROR   = {403: u'访问次数过于频繁'},
    INTERNET_ERROR      = {404: u"网络错误"},
    SYSTEM_ERROR        = {500: u"系统错误"},
    DATA_ERROR          = {405: u"数据错误"},
    MEM_ERROR           = {403: u"内存错误"},
    ERROR               = {501: u"普通错误"},
    ARGS_ERROR          = {406: u'参数出错'},
    SUCCESS             = {200: u'成功'}
)

IMAGE_RESPONSE = dict(
    IMAGE_UPLOAD_ERROR  = {120001: u"上传出错, 数据存储出错"},
    IMAGE_FORMAT_ERROR  = {120002: u"图片格是出错"},
    IMAGE_TYPE_ERROR    = {120003: U'图片类型上传出错'},
    ERROR               = {120404: u"普通错误"},
    SUCCESS             = {200: u"上传成功"}
)

VERSION_RESPONSE = dict(
    VERSION_PARAMS_ERROR  = {130001: u"版本号出错"},
    VERSION_DATA_ERROR    = {130002: u"数据版本格式出错"},
    ERROR                 = {130404: u"获取失败, 不存在这个类型的数据"},
    SUCCESS               = {200: u"版本一致"},
    VERSION_SUCCESS       = {201: u"版本过低"},
    RECOVER_SUCCESS       = {202: u"版本回退"},
)



from .user_response import USER_RESPONSE, ROLE_RESPONSE
from .role_response import ROLE_EXTENDS_RESPONSE

SystemResponse   = type("SystemError", (object, ), SYSTEM_RESPONSE)  # 系统返回信息
UserResponse     = type("UserError"  , (object, ), USER_RESPONSE)    # 用户返回信息
RoleResponse     = type("RoleError"  , (object, ), ROLE_RESPONSE)    # 角色返回信息基础
RoleExtResponse  = type("RoleError"  , (object, ), ROLE_EXTENDS_RESPONSE)  # 角色返回信息扩展
ImageResponse    = type("ImageError" , (object, ), IMAGE_RESPONSE)   # 上传图片返回信息
VersionResponse  = type("VersionError" , (object, ), VERSION_RESPONSE)  # 获取版本错误信息
