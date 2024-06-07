# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 15:17
# @Author  : PXZ
# @Desc    :
from Entity.Bullet import oBulletManager
from Entity.Gun.Base100001 import CGun100001

oGunManager = {
    100001: CGun100001()
}


class CBaseGun:
    iSourceId = 0
    sName = '基础枪械'
    iDamageAdd = 0      # 伤害加成
    iBulletId = 200001

    def __init__(self):
        self.oBullet = oBulletManager[self.iBulletId]