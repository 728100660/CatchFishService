# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 15:31
# @Author  : PXZ
# @Desc    :
from Entity.Bullet import CreateBullet


class CBaseGun:
    iSourceId = 0
    sName = '基础枪械'
    iDamageAdd = 0      # 伤害加成
    iBulletId = 200001
    iLevel = 1      # 枪炮等级
    lCost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     # 各个等级对应的金币消耗

    def GetDamageAdd(self):
        return self.iDamageAdd

    def __init__(self):
        pass

    def GetCost(self):
        return self.lCost[self.iLevel - 1]