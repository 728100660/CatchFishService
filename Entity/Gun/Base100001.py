# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 15:09
# @Author  : PXZ
# @Desc    : 基础枪械
from Entity.Gun import CBaseGun


class CGun100001(CBaseGun):
    iSourceId = 100001
    sName = '基础枪械'
    iDamageAdd = 0      # 伤害加成
    iBulletId = 200001

    def __init__(self):
        super(CBaseGun, self).__init__()