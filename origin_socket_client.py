# -*- coding: utf-8 -*-
# @Time    : 2024/6/6 16:43
# @Author  : PXZ
# @Desc    :
import socket

HOST = 'localhost'
PORT = 8000


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    try:
        while True:
            message = input("Enter your message: ")
            if message == "quit":
                break
            message += "\n"
            client_socket.sendall(message.encode('utf-8'))
            print("发送")
            data = client_socket.recv(1024)
            print("Received:", data.decode('utf-8'))
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
