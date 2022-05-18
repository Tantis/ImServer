# -*- coding: utf-8 -*-
import time
import sys
from twisted.python.log import msg
from twisted.python.logfile import DailyLogFile

class LoggerSetting(DailyLogFile):
    """ 日志文件配置

    """
    def __init__(self, name, directory, exist_postfix = ''):
        super(LoggerSetting, self).__init__(name, directory)

    def close(self):
        """ 关闭 """
        DailyLogFile.close(self)

    def shouldRotate(self):
        """Rotate when the date has changed since last write"""
        cur_date = self.toDate()
        return cur_date > self.lastDate

    def toDate(self, *args):

        return time.localtime(*args)[:4]

class Logger(object):

    @classmethod
    def debug(cls, text):
        code = sys._getframe(1).f_code
        func_tag = '[%s:%d]' % (code.co_name, code.co_firstlineno)
        msg("[DEBUG]" + func_tag + text)

    @classmethod
    def error(cls, text):
        code = sys._getframe(1).f_code
        func_tag = '[%s:%d]' % ( code.co_name, code.co_firstlineno)
        msg("[ERROR]" + func_tag + text)

    @classmethod
    def info(cls, text):
        code = sys._getframe(1).f_code
        func_tag = '[%s:%d]' % ( code.co_name, code.co_firstlineno )
        msg("[INFO]" + func_tag + text)

    @classmethod
    def warning(cls, text):
        code = sys._getframe(1).f_code
        func_tag = '[%s:%d]' % (code.co_name,code.co_firstlineno)
        text = "[WARNING]" + func_tag + text
        msg(text)

