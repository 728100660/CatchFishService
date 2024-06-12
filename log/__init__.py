# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 11:11
# @Author  : PXZ
# @Desc    : 日志
# -*- coding:utf-8 -*-
"""
data：2021/8/31 15:38

"""

import traceback
import re

from log.BaseLog import Logger
from settings import MYSQL_DB


class CLog(object):
    def info(self, msg, save_file=None,
             group_name=MYSQL_DB):  # group_name组名一般为项目名，日志存放在此文件夹下
        if not save_file:
            save_file = get_save_file()
        log_obj = Logger.GetLogger(save_file, group_name)
        # log_obj.info(msg, stacklevel=2)
        print(msg)

    def error(self, msg, save_file=None, group_name=MYSQL_DB):
        if not save_file:
            save_file = get_save_file()
        log_obj = Logger.GetLogger(save_file, group_name)
        log_obj.error(msg, stacklevel=2)

    def warning(self, msg, save_file=None, group_name=MYSQL_DB):
        if not save_file:
            save_file = get_save_file()
        log_obj = Logger.GetLogger(save_file, group_name)
        log_obj.warning(msg, stacklevel=2)


def get_save_file():
    """获取日志存储文件路径，以model_name作为存储文件名"""
    stack_list = traceback.extract_stack()
    filename = stack_list[-3].filename  # 调用位置路径
    re_str = f"(.*?){MYSQL_DB}/{MYSQL_DB}(.*?$)"
    res_obj = re.search(re_str, filename)
    if not res_obj:
        return "default"
    tmp_dir = res_obj.group(2)
    file_name_list = tmp_dir.split("/")
    if not file_name_list or len(file_name_list) == 1:
        return "default"
    save_file = file_name_list[1]      # save_file = modules,script,services,tests,utils
    if save_file != "modules":
        return save_file.split(".")[0]      # 防止出现save_file=xxx.py的情况
    return file_name_list[2].split(".")[0]


LOGGER = CLog()
