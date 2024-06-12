# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 15:17
# @Author  : PXZ
# @Desc    :
from Entity.Bullet.BaseBullet import CBaseBullet

from Entity.Bullet.CBullet200001 import CBullet200001

oBulletManager = {
    200001: CBullet200001()
}

gFactory = {
    200001: CBullet200001,
}


def CreateBullet(iSourceId):
    CBullet = gFactory.get(iSourceId)
    oBullet = CBullet()
    return oBullet
