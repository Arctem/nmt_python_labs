#!/usr/bin/env python

import select
import socket
import sys

def main():
    host = ''
    port = 50000
    backlog = 5
    size = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(backlog)
    inputs = [server, sys.stdin]
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
            else:
                #handle other sockets
                data = s.recv(size)
                if data:
                    #do stuff
                    s.send(data)
                else:
                    #this socket closed
                    try:
                        print("Connection {} closed remotely.".format(s.getpeername()))
                    except OSError:
                        print("A remote connection closed.")
                    s.close()
                    inputs.remove(s)

    server.close()


if __name__ == '__main__':
    main()
