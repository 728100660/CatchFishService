# -*- coding: utf-8 -*-
# @Time    : 2024/6/7 10:50
# @Author  : PXZ
# @Desc    : 捕鱼房间
import random

from Entity.Fish import CBaseFish, CreateFish
from Entity.Gun import CBaseGun
from log import LOGGER
from player import Cplayer
from Entity.Bullet import CBaseBullet
from world import GetPlayer


class CBaseRoom:
    """
    房间对象:
    玩家消耗金币会放入奖金池，当奖金池下降时，捕鱼概率会减少。
    同时，为了保证单个玩家的体验，每个玩家有个累积未捕获鱼的消耗金币数目，金币数目越大，捕鱼概率越大
    捕获鱼的收益由房间倍率以及鱼的基础价值控制
    鱼类移动，也可以考虑只让客户端移动，服务端只负责对象的存活时间，及时销毁即可（这样会有无视阻挡直接射击的风险，但是影响不大）
    问题：成功率过高，没法控制捕鱼概率，生成鱼类方法有问题，没有控制各个种类鱼的数量，数学问题
    """
    iMultiplier = 1000  # 倍率
    iMaxGoldPool = 10000 * iMultiplier  # 金币池上限,放水临界点
    lFish = [400001, 400002, 400003, 400004]    # 可生成的鱼类id
    iLength = 100  # 房间长度
    iWidth = 50  # 房间宽度
    iMaxSize = 20  # 房间最大鱼数

    def __init__(self):
        self.iGoldPool = self.iMaxGoldPool  # 金币池
        self.iLevel = 0  # 等级
        self.dBullet = {}  # 可选子弹列表 {oBullet.GetCost(): oBullet}
        self.dPlayers = {}  # 玩家列表
        self.dPlayerGun = {}    # 玩家对应的枪
        self.dPlayerUse = {}    # 玩家未捕获鱼所消耗金币数
        self.dPlayerShoot = {}  # 玩家射击出的子弹  # 不存盘，重启即消失
        self.dFish = {}  # {iFishIdx: oFish}
        self.dFishTypeNum = {}  # {iFishType: iNum}
        self.iFishIdx = 0  # 自增长鱼序号

    def VerifyShoot(self, oPlayer: Cplayer):
        # 验证金币
        iPid = oPlayer.GetPid()
        iNeedGold = self.dPlayerGun[iPid].GetCost()
        if iNeedGold > oPlayer.GetGold():
            LOGGER.warning(f"金币不足 {iNeedGold} {oPlayer.GetGold()}")
            return False
        return True     # TODO 日后完善

    def NetDoShoot(self, iPid):   # 玩家射击
        oPlayer = GetPlayer(iPid)
        if not self.VerifyShoot(oPlayer):
            print(f"非法射击 {iPid}")
            return
        # 记日志
        # 改状态
        self.dPlayerShoot[iPid] = self.dPlayerShoot.get(iPid, 0) + 1
        oGun = self.dPlayerGun[iPid]
        oPlayer.SetGold(oPlayer.GetGold() - oGun.GetCost() * self.iMultiplier)
        self.iGoldPool += oGun.GetCost()
        self.dPlayerUse[iPid] = self.dPlayerUse.get(iPid, 0) + oGun.GetCost() * self.iMultiplier
        # 记日志
        pass

    def VerifyAttack(self, oPlayer: Cplayer):
        # 验证射出的子弹
        iPid = oPlayer.GetPid()
        iLeftShoot = self.dPlayerShoot.get(iPid, 0)
        if iLeftShoot < 1:
            LOGGER.warning(f"射击次数不足，伤害判定失败 {iLeftShoot}")
            return False
        # 验证碰撞条件
        return True     # TODO 日后完善

    def NetDoAttack(self, iPid, iFishIdx):   # 玩家攻击
        oPlayer = GetPlayer(iPid)
        oFish = self.dFish.get(iFishIdx, None)

        if not self.VerifyAttack(oPlayer):
            LOGGER.warning(f"非法攻击 {iPid}")
            return False
        LOGGER.info(f"player attack: {iPid} {oPlayer.GetGold()} {oFish.iSourceId} {oFish.iBlood}")
        # 改状态
        self.dPlayerShoot[iPid] = self.dPlayerShoot.get(iPid, 0) - 1
        oFish.OnAttack(oPlayer, None)
        res = False
        iRewardGold = 0
        if oFish.IsDead():
            iRewardGold = self.CatchFish(oPlayer, oFish)
            print(f"info 保底捕获 {iPid} {iFishIdx} {iRewardGold} {oFish.GetName()}")
            res = True
        # 判断概率
        fCatchRate = self.GetCatchRate(oPlayer, oFish)
        if random.random() < fCatchRate:
            print(f"info 概率捕获 {iPid} {iFishIdx} {iRewardGold} {fCatchRate} {oFish.GetName()}")
            iRewardGold = self.CatchFish(oPlayer, oFish)
            res = True
        LOGGER.info(f"player attack res: {iPid} {oPlayer.GetGold()} {oFish.iBlood} {res}")
        if res:
            print(f"捕获鱼成功 {iPid} {iFishIdx} {iRewardGold}")
            del self.dFish[iFishIdx]
        return res

    def GetCatchRate(self, oPlayer: Cplayer, oFish: CBaseFish):   # 获取捕获概率
        iPid = oPlayer.GetPid()
        iFishReward = oFish.iGold * self.iMultiplier
        if self.iGoldPool <= iFishReward:
            LOGGER.warning(f"金币池不足 {self.iGoldPool} {iFishReward}")
            return 0
        # 基础概率 * 角色概率加成 * 总池子抽放水 * 单个玩家优化体验概率
        iUseGold = self.dPlayerUse[iPid]
        fUseRate = max(iUseGold / iFishReward, 1)   # 单个玩家优化体验概率
        fRate = oFish.GetBaseRate() * (self.iGoldPool / self.iMaxGoldPool) * \
                oPlayer.GetRateAdd() * fUseRate
        return fRate

    def CatchFish(self, oPlayer: Cplayer, oFish: CBaseFish):   # 玩家捕获
        iPid = oPlayer.GetPid()
        iRewardGold = oFish.iGold * self.iMultiplier
        LOGGER.info(f"player catch: {iPid} {oPlayer.GetGold()} {iRewardGold}")
        oPlayer.SetGold(oPlayer.GetGold() + iRewardGold)
        self.iGoldPool -= iRewardGold
        self.dPlayerUse[iPid] = 0   # 清空未捕获鱼所消耗的金币
        self.dFishTypeNum[oFish.iSourceId] -= 1
        LOGGER.info(f"player catch res: {oPlayer.GetPid()} {oPlayer.GetGold()}")
        return iRewardGold

    def EnterRoom(self, iPid):
        print(f"玩家 {iPid} 进入房间")
        if iPid not in self.dPlayerGun:
            self.dPlayerGun[iPid] = CBaseGun()

    def Update(self):       # 类似unity，每秒/帧更新
        while len(self.dFish) < self.iMaxSize:
            self.GeneralFish()
        for idx, oFish in self.dFish.items():
            oFish.Move()
            # print(f"鱼类移动 {idx} {oFish.tPos}")

    def GeneralFish(self):  # 生成鱼类
        x = random.randint(0, self.iLength)
        y = random.randint(0, self.iWidth)
        # 种类数目限制
        lTmpFish = self.lFish.copy()
        iFish = random.choice(lTmpFish)
        while iFish == 400003 and self.dFishTypeNum.get(iFish, 0) >= 3:     # 蝙蝠鱼数量不能超过3
            lTmpFish.remove(iFish)
            iFish = random.choice(lTmpFish)
        while iFish == 400004 and self.dFishTypeNum.get(iFish, 0) >= 1:     # 锤头鲨数量不能超过1
            lTmpFish.remove(iFish)
            iFish = random.choice(lTmpFish)

        oFish = CreateFish(iFish, x, y)
        self.iFishIdx += 1
        self.dFish[self.iFishIdx] = oFish
        self.dFishTypeNum[iFish] = self.dFishTypeNum.get(iFish, 0) + 1
        print(f"生成鱼类 {self.iFishIdx} {iFish} {x} {y}")

    def load(self, data):
        self.iGold = data['iGold']
        self.iLevel = data['iLevel']

    def save(self):
        return {
            'iGold': self.iGold,
            'iLevel': self.iLevel
        }