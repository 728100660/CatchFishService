# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 14:54
# @Author  : PXZ
# @Desc    :
from Entity.Bullet import CBaseBullet
from player import Cplayer


class CBaseFish:
    """
    鱼类对象
    目前没有考虑倍率情况
    血量上限就是保底，所以保底所消耗金币一定要比鱼获得金币高，
    """
    iSourceId = 0  # 鱼资源源id
    sName = ''  # 名称
    iMaxBlood = 0  # 血量上限
    iLevel = 0  # 等级
    fBaseRate = 0  # 基础捕获概率范围  0-100
    iGold = 0  # 鱼金币价值

    def __init__(self, x, y):
        self.iBlood = self.iMaxBlood  # 当前血量
        self.tPos = (x, y)

    def GetBaseRate(self):
        return self.fBaseRate / 100

    def OnInit(self):   # 初始化：位置信息等
        pass

    def OnAttack(self, oPlayer: Cplayer, oBullet: CBaseBullet):   # 被玩家攻击
        self.iBlood -= 1
        pass

    def IsDead(self):   # 是否死亡
        return self.iBlood <= 0

    def OnCatch(self, oPlayer):   # 被玩家捕获
        pass

    def Move(self):     # 难点，
        pass

    def GetName(self):
        return self.sName