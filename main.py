# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
枪械：1000 01
子弹: 2000 01
捕鱼房间: 3000 01
"""


class CRank:
    """
    排名
    LItems: []
    """


class CBag:
    """
    背包
    LItems: []
    """

class CPlayer:
    """
    玩家
    gold: 金币
    level: 等级
    oBag: 背包
    """

class CWorld:
    """
    主体
    Players: []
    Rooms: []
    """

class CRooms:
    """
    房间
    rate: 倍率
    iGoldPool: 金币总池子
    lFish: 鱼列表
    oPlayers: []
    oNet: 网络模块（玩家进入是addUser方法）
    """