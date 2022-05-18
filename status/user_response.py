#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved
# 错误信息预留从10001 ~ 11000
# 定义基础错误信息
# 后三位200 = 成功 500=失败
USER_RESPONSE = dict(
    LOGIN_ERROR               = {10001: u"玩家登陆错误"},
    USER_EXISTS_ERROR         = {10002: u"账号已经存在"},
    USER_PASS_ERROR           = {10003: u"登陆用户或密码出错"},
    USER_PASS_ERROR_WHERE     = {10004: u"密码设置条件不符合"},
    USER_REPEAT_ERROR         = {10005: u"登陆次数过多"},
    USER_ACCOUNT_ERROR_WHERE  = {10006: u"设置账户不符合条件"},
    USER_NOT_EXISTS_ERROR     = {10007: u"用户账户不存在"},
    USER_TOKEN_GEN_ERROR      = {10008: u"生成TOKEN失败"},
    USER_SUCCESS              = {200: u"登陆成功"},
    USER_REGISTER_SUCCESS     = {200: u"注册成功"},
    USER_FAILD                = {10500: u"登陆失败"}
)

ROLE_RESPONSE = dict(
    ROLE_EXISTS_ERROR = {11002: u"角色已经存在"},
    ROLE_DELETE_ERROR = {11003: u'选择角色出错，角色已经被删除'},
    ROLE_SUCCESS      = {200: u"成功"},
    ROLE_FAILD        = {500: U'失败'},
)