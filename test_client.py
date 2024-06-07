# -*- coding: utf-8 -*-
# @Time    : 2024/6/6 16:31
# @Author  : PXZ
# @Desc    :
from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver


class GameClient(LineReceiver):
    def connectionMade(self):
        print("Connected to server")
        msg = input("Enter message: ")
        self.sendLine(msg.encode('utf-8'))

    def lineReceived(self, line):
        message = line.decode('utf-8')
        print(f"Received from server: {message}")


class GameClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return GameClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed:", reason.getErrorMessage())
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost:", reason.getErrorMessage())
        reactor.stop()


if __name__ == "__main__":
    reactor.connectTCP("localhost", 8000, GameClientFactory())
    reactor.run()
