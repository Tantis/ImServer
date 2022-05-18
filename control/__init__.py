#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2018 yu.liu <showmove@qq.com>
# All rights reserved


""" 数据控制类

"""
import time 
import tablib
from inspect import isclass
from contextlib import contextmanager
from control.control_mysql import mysqlOperation
from control.control_redis import redisOperation

@contextmanager
def cost_time():
    t1 = time.time()
    yield
    t2 = time.time()
    print('cost time=', t2-t1)

def _reduce_datetimes(row):
    """Receives a row, converts datetimes to strings."""

    row = list(row)

    for i in range(len(row)):
        if hasattr(row[i], 'isoformat'):
            row[i] = row[i].isoformat()
    return tuple(row)


def isexception(obj):
    """Given an object, return a boolean indicating whether it is an instance
    or subclass of :py:class:`Exception`.
    """
    if isinstance(obj, Exception):
        return True
    if isclass(obj) and issubclass(obj, Exception):
        return True
    return False


class Export(object):
    """ 转换数据格式

    """
    def __init__(self, keys, rows):
        
        self.rows = rows
        self.headers = keys

    def export(self, format, **kwargs):
        """Export the RecordCollection to a given format (courtesy of Tablib)."""
        # return self.dataset.export(format, **kwargs)
        data = tablib.Dataset()
        data.headers = self.headers
        for row in self.rows:
            row = _reduce_datetimes(row.values())
            data.append(row)
        res = data.export(format, **kwargs)
        print(res)
        return res

if __name__ == "__main__":
    
    with cost_time():
        p = Export(["a", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8"], 
        [{"a": "b", "b1": "c", "b2": "c", "b3": "c", "b4": "c", "b5": "c", "b6": "c", "b7": "c", "b8": "c"} for i in xrange(10)])
        p.export("json")

        # time.sleep(0.5)