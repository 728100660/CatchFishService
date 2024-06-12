# -*- coding: utf-8 -*-
# @Time    : 2024/6/11 16:36
# @Author  : PXZ
# @Desc    : 网络模块
from Entity.room import CBaseRoom


class CNet:

    def __init__(self):
        self.oCtrl = None
        self.dProtocol = {
            101: self.EnterRoom,
        }

    def EnterRoom(self):
        # 解析协议获取参数
        # 调用oRoom的EnterRoom函数
        pass