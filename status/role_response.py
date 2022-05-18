#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved
# 错误信息预留从10001 ~ 11000
# 定义基础错误信息
# 后三位200 = 成功 500=失败
ROLE_EXTENDS_RESPONSE = dict(
    SETTING_VALUE_ERROR       = {14001: u"设置错误,设置的键值不符合规则"},
    SETTING_NAME_ERROR        = {14002: u"设置属性错误"},
)
