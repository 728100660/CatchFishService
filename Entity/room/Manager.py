# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 11:41
# @Author  : PXZ
# @Desc    :
import random

from Entity.room import CBaseRoom
from Entity.room.Net import CNet


class CManager:

    def __init__(self):
        self.oNet = CNet()
        self.oGame = CBaseRoom()
        self.dFuncMap = {
            101: self.oGame.EnterRoom,
            121: self.NetDoShoot,
            122: self.NetDoAttack,
        }

    def NetDoShoot(self, lArgs):
        iPid = lArgs[0]
        self.oGame.NetDoShoot(iPid)

    def NetDoAttack(self, lArgs):
        iPid = int(lArgs[0])
        iFishIdx = int(lArgs[1])
        self.oGame.NetDoAttack(iPid, iFishIdx)

    def onMsg(self, iType, lArgs):
        oFunc = self.dFuncMap.get(iType)
        oFunc(lArgs)


if __name__ == '__main__':
    oManager = CManager()
    oManager.oGame.EnterRoom(1)
    while True:
        oManager.oGame.Update()
        oManager.onMsg(121, [1])
        oManager.onMsg(122, [1, random.choice(list(oManager.oGame.dFish.keys()))])
        sInput = input("是否继续 n:否")
        if sInput in ['n', 'N']:
            break