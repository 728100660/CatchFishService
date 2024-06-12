# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 14:54
# @Author  : PXZ
# @Desc    :
from .BaseFish import CBaseFish
# 导表开始
from .Fish400001 import CFish400001
from .Fish400002 import CFish400002
from .Fish400003 import CFish400003
from .Fish400004 import CFish400004

gFactory = {
    400001: CFish400001,
    400002: CFish400002,
    400003: CFish400003,
    400004: CFish400004
}


# 导表结束

def CreateFish(iSourceId, x, y):
    return gFactory[iSourceId](x, y)
