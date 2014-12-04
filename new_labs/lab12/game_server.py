#!/usr/bin/env python

import select
import socket
import sys
import pickle
from player import Player
from monster import Monster

DATA_SIZE = 1024 * 10 #10 kilobytes max per message

def create_server_sock(port=50000, host='', backlog=5):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((host, port))
  server.listen(backlog)
  return server

def main():
  inputs = []
  player_sockets = []

  server = create_server_sock()

  inputs.append(server)
  inputs.append(sys.stdin)
  running = True

  while running:
    input_ready, output_ready, except_ready = select.select(inputs + player_sockets, [], [])
    
    for s in input_ready:
      if s == server:
        client, address = server.accept()
        if len(player_sockets) < 2:
          print('Received connection from {}.'.format(address))
          player_sockets.append(client)
        else:
          print('Rejecting connection from {}.'.format(address))
          client.sendall(b'too many players\n')
          client.close()

      elif s == sys.stdin:
        #handle standard input
        junk = sys.stdin.readline().strip()
        if junk == 'quit':
          print('Closing server.')
          running = False

      else:
        #handle other sockets
        try:
          data = s.recv(DATA_SIZE)
        except (ConnectionResetError, TimeoutError) as e:
          #count as closed if other connection terminated early
          data = None
        print(data)
        if not data:
          #this socket closed or handle_message returned False
          print("Connection closed remotely.")
          player_sockets.remove(s)
          s.close()
        else:
          for sock in player_sockets:
            if sock != s:
              sock.sendall(data)

          

  server.close()


if __name__ == '__main__':
  main()
