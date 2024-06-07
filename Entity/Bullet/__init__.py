# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 15:17
# @Author  : PXZ
# @Desc    :
from Entity.Bullet.Bullet200001 import Bullet200001

oBulletManager = {
    200001: Bullet200001()
}


class CBaseBullet:
    iSourceId = 0
    sName = '基础子弹'
    iDamageAdd = 1      # 伤害加成
    iCost = 1          # 消耗金币

    def __init__(self):
        pass

    def GetCost(self):
        return self.iCost