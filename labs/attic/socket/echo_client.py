#!/usr/bin/env python

import socket

def main():
    HOST = 'arctem.com'
    PORT = 50000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    running = True
    while running:
        msg = input("Input a message to echo: ")
        if msg == 'quit':
            running = False
        msg = msg.encode()
        s.sendall(msg)
        data = s.recv(1024)
        if not data:
            print("Remote server closed connection.")
            running = False
        else:
            data = data.decode()
            print('Received {}'.format(data))
    s.close()

if __name__ == '__main__':
    main()
