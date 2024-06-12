# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 14:00
# @Author  : PXZ
# @Desc    :
from Entity.Fish.BaseFish import CBaseFish


class CFish400001(CBaseFish):
    iSourceId = 400001  # 鱼资源源id
    sName = '小黄鱼'  # 名称
    iMaxBlood = 20  # 血量上限
    iLevel = 1  # 等级
    fBaseRate = 40  # 基础捕获概率范围  0-100
    iGold = 1  # 鱼金币价值 iMaxBlood / 2