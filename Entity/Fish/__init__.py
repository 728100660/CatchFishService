# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 14:54
# @Author  : PXZ
# @Desc    :
# 导表开始
from Entity.Bullet import CBaseBullet
from player import Cplayer


# 导表结束

class CBaseFish:
    """
    鱼类对象
    """
    iSourceId = 0  # 鱼资源源id
    sName = ''  # 名称
    iMaxBlood = 0  # 血量上限
    iLevel = 0  # 等级
    fBaseRate = 0  # 基础捕获概率
    iGold = 0  # 鱼金币价值

    def __init__(self):
        self.iBlood = self.iMaxBlood  # 当前血量

    def OnInit(self):   # 初始化：位置信息等
        pass

    def OnAttack(self, oPlayer: Cplayer, oBullet: CBaseBullet):   # 被玩家攻击
        pass

    def IsDead(self):   # 是否死亡
        return self.iBlood <= 0

    def OnCatch(self, oPlayer):   # 被玩家捕获
        pass

    def Move(self):     # 难点
        pass