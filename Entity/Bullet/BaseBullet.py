# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 15:28
# @Author  : PXZ
# @Desc    :


class CBaseBullet:
    iSourceId = 0
    sName = '基础子弹'
    iDamageAdd = 1      # 伤害加成
    iCost = 1          # 消耗金币

    def __init__(self):
        pass

    def GetCost(self):
        return self.iCost