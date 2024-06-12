# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 14:57
# @Author  : PXZ
# @Desc    :
import platform


def IsWindows():
    system_name = platform.system()
    if system_name == "Windows":
        return True
    else:
        return False