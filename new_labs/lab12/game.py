#!/usr/bin/env python

import socket
import pickle
import tkinter
from threading import Thread
from monster import Monster
from party import Party

DATA_SIZE = 1024 * 10 #10 kilobytes max per messagep

class Frame(tkinter.Frame):
  def __init__(self, parent, sock):
    tkinter.Frame.__init__(self, parent, background="white")
     
    self.parent = parent
    self.sock = sock

    self.init_party()
    
    self.initUI()
  
  def initUI(self):
    self.parent.title("Battle")
    button = tkinter.Button(self, text='Send Monster', fg='red',
    command = self.send_monster)
    button.grid(row=0, column=0, columnspan=4)

    switch = tkinter.Button(self, text='Switch Monster',
      command=lambda: print("hello"))
    switch.grid(row=3, column=0)

    move = tkinter.Button(self, text='Use Move')
    move.grid(row=3, column=3)
    
    self.grid(row=0, column=0)

  def init_party(self):
    monsters = [Monster(x) for x in ['Tyler', 'Russell', 'Chris']]
    self.party = Party(monsters)


  def send_monster(self):
    data = pickle.dumps(self.party)
    self.sock.sendall(data)
    data = self.sock.recv(DATA_SIZE)
    if not data:
      print("Remote server closed connection.")
      running = False
    else:
      data = pickle.loads(data)
      if isinstance(data, Monster):
        print('Opponent\'s monster is {}.'.format(data.name))
      if isinstance(data, Party):
        print("Opponent's party has {} monsters!".format(len(data.party)))
        print("Opponent's active monster is {}.".format(data.active.name))
      else:
        print('Received {}'.format(data))

def toggle(event):
  event.widget.grid_remove()


def main():
  HOST = 'localhost'
  PORT = 50000
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  print('Connected to server.')

  root_window = tkinter.Tk()
  root_window.geometry("250x150+300+300")
  frame = Frame(root_window, s)
  print('Created window.')
  root_window.mainloop()

if __name__ == '__main__':
  main()
