# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 14:07
# @Author  : PXZ
# @Desc    :

from Entity.Fish.BaseFish import CBaseFish


class CFish400003(CBaseFish):
    iSourceId = 400003  # 鱼资源源id
    sName = '蝙蝠鱼'  # 名称
    iMaxBlood = 100  # 血量上限
    iLevel = 1  # 等级
    fBaseRate = 5  # 基础捕获概率范围  0-100
    iGold = 10