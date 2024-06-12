# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 14:07
# @Author  : PXZ
# @Desc    :
from Entity.Fish.BaseFish import CBaseFish


class CFish400002(CBaseFish):
    iSourceId = 400002  # 鱼资源源id
    sName = '小蓝鱼'  # 名称
    iMaxBlood = 30  # 血量上限
    iLevel = 1  # 等级
    fBaseRate = 18  # 基础捕获概率范围  0-100
    iGold = 15  # 鱼金币价值 iMaxBlood / 2