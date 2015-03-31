#!/usr/bin/env python

import select
import socket
import sys

def main():
    HOST = 'arctem.com'
    PORT = 50001
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    running = True
    inputs = [sock, sys.stdin]
    
    while running:
        input_ready, output_ready, except_ready = select.select(inputs, [], [])

        for s in input_ready:
            if s == sock:
                data = s.recv(1024)
                if not data:
                    print("Remote server closed connection.")
                    running = False
                else:
                    data = data.decode()
                    print("Received: {}".format(data.strip()))
            elif s == sys.stdin:
                msg = sys.stdin.readline().strip()
                if msg == 'quit':
                    running = False
                elif msg != '':
                    msg += '\n'
                    msg = msg.encode()
                    sock.sendall(msg)
        
    s.close()

if __name__ == '__main__':
    main()
