# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 15:12
# @Author  : PXZ
# @Desc    : 子弹200001
from Entity.Bullet import CBaseBullet


class CBullet200001(CBaseBullet):
    iSourceId = 200001
    sName = '基础子弹'
    iDamageAdd = 1      # 伤害加成

    def __init__(self):
        super(CBaseBullet, self).__init__()