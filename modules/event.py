#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2016 yu.liu <showmove@qq.com>
# All rights reserved

"""事件驱动模块

主要用于层次管理
```

@Event.execute(target)
def func():
    return {"data": 123}

```

"""
import inspect
from functools import wraps


class Event(object):
    """
    事件驱动模块
    """
    @staticmethod
    def execute(target):
        """装饰事件
        :params targer    :  必要。目标函数
        """
        def control(func, *args, **kwarg): 
            result = lambda x: target(x)
            def __console(*ag, **kw):
                response = func(*ag, **kw)
                return result(response)
            return __console
        return control

    @staticmethod
    def befor(target, *argsv, **kwargs):
        """ 函数执行前函数

        """
        def control(func, *args, **kwarg):
            @wraps(func)
            def __console(*ag, **kw):
                print(func.__name__, ag, kw)
                flag, response = target(*argsv, **kwargs)
                if not flag:
                    return response
                kw["response_func"] = response
                return func(*ag, **kw)
            return __console
        return control
    
    @staticmethod
    def after(target, *argsv, **kwargs):
        """ 函数执行之后是否执行某函数

        """
        def control(func, *args, **kwarg): 
            result = lambda x: target(x)
            def __console(*ag, **kw):
                response = func(*ag, **kw)
                kwargs["response_func"] = response
                return result(kwargs)
            return __console
        return control

# 使用案例

class EventControl(object):
    """事件驱动方法

    用户定义什么事件既可以使用什么事件
    """
    @classmethod
    def befor(cls, **kwargs):
        print(kwargs)
        return False, 100 - 9

    @classmethod
    def after(cls, kwargs):
        print(kwargs)
        return kwargs["response_func"]


@Event.after(EventControl.after)
@Event.befor(EventControl.befor)
def main(a,b,c,**kwargs):
    print(a, b, c)
    print(kwargs)
    return kwargs

if __name__ == "__main__":

    main(1,2,3, x='u')