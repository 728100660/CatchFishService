# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 11:30
# @Author  : PXZ
# @Desc    :
# -*- coding:utf-8 -*-
#
# Author:jing
# Date: 2020/5/13
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from settings import LOGGER_BASE_PATH


def formatter(attr_dict, attr):
    if not attr_dict:
        return "-"
    else:
        attr_val = attr_dict.get(attr)
        return attr_val if attr_val != None else "-"


class ErrorFilter(logging.Filter):

    def filter(self, record):
        if record.levelno >= logging.WARNING:
            return True
        return False


class Logger(object):
    base_path = LOGGER_BASE_PATH
    __fmt = ("%(asctime)s %(levelname)s %(filename)s-%(lineno)d "
             "pid-%(process)d: %(request_uid)s %(message)s")
    __console_fmt = ('%(asctime)s %(levelname)s File "%(pathname)s", line '
                     '%(lineno)d p-%(process)d-t-%(thread)d: %(message)s')
    __date_fmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=__fmt, datefmt=__date_fmt)
    console_formatter = logging.Formatter(__console_fmt, __date_fmt)

    loggers = {}

    @classmethod
    def ensure_logger_path(cls, group):
        path = os.path.join(cls.base_path, group)
        ensure_dir(path)
        return path

    @classmethod
    def _init_logger(cls, name, group):
        if group is None:
            group = name

        path = cls.ensure_logger_path(group)
        log_file = os.path.join(path, f'{name}.log')

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        handler = RotatingFileHandler(
            log_file, mode='a', maxBytes=100 * 1024 * 1024, backupCount=3)
        handler.setFormatter(cls.formatter)
        logger.addHandler(handler)

        err_file = os.path.join(path, "error.log")
        err_handler = RotatingFileHandler(err_file, mode='a', maxBytes=100 * 1024 * 1024, backupCount=3)
        # 错误日记单独记录到error.log
        err_handler.addFilter(ErrorFilter())
        err_handler.setFormatter(cls.formatter)
        logger.addHandler(err_handler)

        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(cls.console_formatter)
        logger.addHandler(console)

        # logger.addFilter(DecoFilter())

        logger.propagate = False  # stop passing events to higher level loggers

        return logger

    @classmethod
    def GetLogger(cls, name, group=None) -> logging.Logger:

        if name not in cls.loggers:
            logger = cls._init_logger(name, group)
            cls.loggers[name] = logger
        return cls.loggers[name]


def ensure_dir(path: str):
    """if not exist, create one"""
    os.makedirs(path, exist_ok=True)
    return path


log = Logger.GetLogger('default', 'power_iot')
err = Logger.GetLogger('error', 'power_iot')
slowlog = Logger.GetLogger('slow', 'power_iot')
