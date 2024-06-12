# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 10:49
# @Author  : PXZ
# @Desc    :
from Utils import IsWindows
from player import Cplayer, CreatePlayer

gPlayerMap = {}     # {pid: oPlayer}


def GetPlayer(iPid):
    oPlayer = gPlayerMap.get(iPid)
    if oPlayer is None and IsWindows():
        oPlayer = CreatePlayer(iPid, '测试玩家')
        gPlayerMap[iPid] = oPlayer
        return oPlayer
    if not oPlayer:
        print(f"error玩家 {iPid} 不存在")
    return oPlayer