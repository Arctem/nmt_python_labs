#!/usr/bin/env python

import socket
import pickle
from monster import Monster

DATA_SIZE = 1024 * 10 #10 kilobytes max per message

def main():
    HOST = 'localhost'
    PORT = 50000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    running = True
    while running:
        msg = input("Input a name for your monster: ")
        if msg == 'quit':
            running = False
        monster = Monster(msg)
        monster = pickle.dumps(monster)
        s.sendall(monster)
        data = s.recv(DATA_SIZE)
        if not data:
            print("Remote server closed connection.")
            running = False
        else:
            data = pickle.loads(data)
            print('Received {}'.format(data))
    s.close()

if __name__ == '__main__':
    main()
