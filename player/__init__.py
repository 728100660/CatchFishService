# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 10:30
# @Author  : PXZ
# @Desc    :
from bag import CBag
from common.save_obj import CSaveObj


class Cplayer(CSaveObj):
    """
    玩家对象
    """

    def __init__(self, iPid, sName):
        super(Cplayer, self).__init__()
        self.iPid = iPid  # 玩家id
        self.sName = sName  # 名称
        self.iGold = 10000  # 金币
        self.iLevel = 1  # 等级
        self.fRateAdd = 1  # 捕获概率加成
        self.oBag = CBag()

    def GetRateAdd(self):
        return self.fRateAdd

    def SetRateAdd(self, fRateAdd):
        self.fRateAdd = fRateAdd

    def GetPid(self):
        return self.iPid

    def GetGold(self):
        return self.iGold

    def SetGold(self, iGold):
        self.iGold = iGold
        print(f"玩家金币 {self.iGold}")

    def GetLevel(self):
        return self.iLevel

    def SetLevel(self, iLevel):
        self.iLevel = iLevel

    def GetBag(self):
        return self.oBag

    def load(self, data):
        self.iGold = data['iGold']
        self.iLevel = data['iLevel']
        self.oBag.load(data['oBag'])

    def save(self):
        return {
            'iGold': self.iGold,
            'iLevel': self.iLevel,
            'oBag': self.oBag.save()
        }

def CreatePlayer(iPid, sName):
    oPlayer = Cplayer(iPid, sName)
    return oPlayer