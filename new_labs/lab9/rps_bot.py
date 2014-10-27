#!/usr/bin/env python

import select
import socket
import sys
import random

bot_names = ['larry', 'moe', 'curly', 'shemp', 'joe']

def win():
    print('I won!')
    return 'y'

def lose():
    print('I lost! :(')
    return 'y'

def dc():
    print('My opponent left.')
    return 'y'

funcs = {
    'name' : lambda x: 'rps_bot',
    'taken' : lambda x: '{}_bot'.format(random.choice(bot_names)),
    'wait' : lambda x: None,
    'opponent' : lambda x: print('Matched with opponent {}.'.format(x[0])),
    'play' : lambda x: random.choice('rps'),
    'tie' : lambda x: None,
    'win' : lambda x: win(),
    'lose' : lambda x: lose(),
    'disconnect' : lambda x: dc()
}

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
                    cmd = data.split()[0]
                    if cmd in funcs.keys():
                        msg = funcs[cmd](data.split()[1:])
                        if msg:
                            sock.sendall(msg.encode())
                    print("Received: {}".format(data))
            elif s == sys.stdin:
                msg = sys.stdin.readline().strip()
                if msg == 'quit':
                    running = False
                else:
                    msg = msg.encode()
                    sock.sendall(msg)
        
    s.close()

if __name__ == '__main__':
    main()
