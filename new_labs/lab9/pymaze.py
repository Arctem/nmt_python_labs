#!/usr/bin/env python

import select
import socket
import sys
from maze import Maze

def main():
    host = ''
    port = 50002
    backlog = 5
    size = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(backlog)

    inputs = [server, sys.stdin]
    mazes = {}
    names = {}
    running = True
    while running:
        input_ready, output_ready, except_ready = select.select(inputs, [], [])
        
        for s in input_ready:
            if s == server:
                client, address = server.accept()
                print("Received connection from {}.".format(address))
                inputs.append(client)

            elif s == sys.stdin:
                #handle standard input
                junk = sys.stdin.readline().strip()
                if junk == 'quit':
                    print("Closing server.")
                    running = False
                if junk == 'users':
                    print("Users: {}".format(list(map(lambda u: names[u], names))))
            else:
                #handle other sockets
                try:
                    data = s.recv(size)
                except ConnectionResetError:
                    #count as closed if other connection terminated early
                    data = None

                if data:
                    data = data.decode().strip()
                    if s not in names.keys():
                        names[s] = data
                        mazes[s] = Maze()
                        s.sendall(mazes[s].look_around().encode())
                    else:
                        pass
                        
                else:
                    #this socket closed
                    print("Connection {} closed remotely.".format(names[s]))
                    s.close()
                    del names[s]
                    del mazes[s]
                    inputs.remove(s)


    server.close()


if __name__ == '__main__':
    main()
