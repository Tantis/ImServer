#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2019 yu.liu <showmove@qq.com>
# All rights reserved
""" REDIS 设计

"""
import os

# 基础定义配置
ROLE_EQUIPMENT_NUMBER = 10     # 玩家装备格子数量
PROPS_BACKPACK = 40            # 背包道具格子总数量配置
PROPS_EQUIPMENT_BACKPACK = 20  # 背包装备格子总数配置
PROPS_WAREHOUSE = 40           # 仓库道具格子配置
PROPS_WAREHOUSE_EQUIPMENT = 20 # 仓库装备格子配置

USER_CONNECTION_NUMBER = "user:connection:number:%(server)s:hash" # 连接服务器的用户数量
USER_FRIENDS_SET = "user:friend:%(user_id)s"
USER_GROUPS_SET = "user:group:items:%(group_id)s:set"


# REDIS订阅列表
CHANNEL_COMMANDS = "game:channel:commands" # 指令 (1=类型， 2=指令, 3=其他信息)

