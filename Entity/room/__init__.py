# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 10:50
# @Author  : PXZ
# @Desc    : 捕鱼房间
from Entity.Fish import CBaseFish
from log import LOGGER
from player import Cplayer
from Entity.Bullet import CBaseBullet


class CBaseRoom:
    """
    房间对象
    """
    iMultiplier = 1000  # 倍率
    iMaxGoldPool = 10000  # 金币池上限,放水临界点

    def __init__(self):
        self.iGoldPool = 0  # 金币池
        self.iLevel = 0  # 等级
        self.dBullet = {}  # 可选子弹列表 {oBullet.GetCost(): oBullet}
        self.dPlayers = {}
        self.dPlayerGun = {}

    def VerifyAttack(self):
        return True     # TODO 日后验证

    def DoAttack(self, oPlayer: Cplayer, oBullet: CBaseBullet, oFish: CBaseFish):   # 玩家攻击
        if not self.VerifyAttack():
            LOGGER.error(f"非法攻击{oPlayer.GetPid()}")
            return False
        LOGGER.info(f"player attack: {oPlayer.GetPid()} {oFish.iSourceId} {oFish.iBlood} {oBullet.iSourceId}")
        oFish.OnAttack(oPlayer, oBullet)
        if oFish.IsDead():
            self.CatchFish(oPlayer, oFish)
            return True
        return True

    def GetCatchRate(self, oPlayer: Cplayer, oFish: CBaseFish):   # 获取捕获概率
        if self.iGoldPool <= oFish.iGold:
            LOGGER.warning(f"金币池不足 {self.iGoldPool} {oFish.iGold}")
            return 0
        fRate = oFish.fBaseRate * (self.iGoldPool / self.iMaxGoldPool)
        return fRate

    def CatchFish(self, oPlayer: Cplayer, oFish: CBaseFish):   # 玩家捕获
        LOGGER.info(f"player catch: {oPlayer.GetPid()} {oPlayer.GetGold()} {oFish.iGold}")
        oPlayer.SetGold(oPlayer.GetGold() + oFish.iGold)
        self.iGoldPool -= oFish.iGold
        LOGGER.info(f"player catch res: {oPlayer.GetPid()} {oPlayer.GetGold()}")

    def load(self, data):
        self.iGold = data['iGold']
        self.iLevel = data['iLevel']

    def save(self):
        return {
            'iGold': self.iGold,
            'iLevel': self.iLevel
        }