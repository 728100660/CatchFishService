from twisted.internet import reactor, protocol


clients = []


# 定义一个 Echo 协议
class Echo(protocol.Protocol):

    def dataReceived(self, data):
        # 当接收到数据时，将数据发送回客户端
        # self.transport.write(data)
        for client in clients:
            client.transport.write(data)

    def connectionMade(self):
        clients.append(self)


# 定义一个 Echo 协议工厂
class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


# 启动服务器
def main():
    reactor.listenTCP(8000, EchoFactory())
    reactor.run()


if __name__ == '__main__':
    main()