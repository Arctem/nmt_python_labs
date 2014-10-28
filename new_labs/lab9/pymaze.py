#!/usr/bin/env python

import select
import socket
import sys
import pickle
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

    step_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    step_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    step_server.bind((host, port + 1))
    step_server.listen(backlog)

    time_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    time_server.bind((host, port + 2))
    time_server.listen(backlog)

    inputs = [server, step_server, time_server, sys.stdin]
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

            elif s == step_server:
                client, address = s.accept()
                print("Received step leaderboard request from {}.".format(address))
                for line in get_step_leaderboard():
                    line += "\n"
                    client.sendall(line.encode())
                client.close()

            elif s == time_server:
                client, address = s.accept()
                print("Received time leaderboard request from {}.".format(address))
                for line in get_time_leaderboard():
                    line += "\n"
                    client.sendall(line.encode())
                client.close()

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
                        print("{} identified as {}.".format(s.getpeername(), data))
                        names[s] = data
                        mazes[s] = Maze()
                        s.sendall(mazes[s].look_around().encode())
                    else:
                        if mazes[s].make_move(data):
                            if mazes[s].success():
                                time = mazes[s].get_elapsed()
                                steps = mazes[s].steps
                                print("{} won with {} steps in {} seconds.".format(names[s], steps, time))
                                win_string = 'win {} {}'.format(steps, time)
                                manage_records(names[s], steps, time)
                                s.sendall(win_string.encode())
                                s.close()
                                del names[s]
                                del mazes[s]
                                inputs.remove(s)
                            else:
                                s.sendall(mazes[s].look_around().encode())
                        else:
                            s.sendall(b'invalid')
                        
                else:
                    #this socket closed
                    if s in names.keys():
                        print("Connection {} closed remotely.".format(names[s]))
                    else:
                        print("An unidentified client disconnected.")
                    s.close()
                    del names[s]
                    del mazes[s]
                    inputs.remove(s)


    server.close()


time_records = []
step_records = []
MAX_RECORDS = 50

try:
    time_records = pickle.load(open('time_records.dmp', 'rb'))
except FileNotFoundError:
    print("Could not load time records file.")

try:
    step_records = pickle.load(open('step_records.dmp', 'rb'))
except FileNotFoundError:
    print("Could not load step records file.")

def manage_records(name, steps, time):
    time_records.append((time, name))
    step_records.append((steps, name))

    time_records.sort()
    step_records.sort()

    time_records = time_records[:MAX_RECORDS]
    step_records = step_records[:MAX_RECORDS]

    pickle.dump(time_records, open('time_records.dmp', 'wb'))
    pickle.dump(step_records, open('step_records.dmp', 'wb'))

def get_step_leaderboard():
    if step_records:
        for s in step_records:
            yield "{}:\t{}".format(s[1], s[0])
    else:
         yield "No records yet."

def get_time_leaderboard():
    if time_records:
        for t in time_records:
            yield "{}:\t{}".format(t[1], t[0])
    else:
         yield "No records yet."

if __name__ == '__main__':
    main()
