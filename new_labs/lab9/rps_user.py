import rps_mom as mom

class User:
    
    def __init__(self, socket):
        self.socket = socket
        self.name = None
        self.last = None
        self.opponent = None
        self.play = None
        self.partial_msg = None
        self.request_name()

    def send(self, msg):
        msg += '\n'
        self.socket.sendall(msg.encode())
        self.last = msg.strip()

    def recv(self, msg):
        if not msg:
            return False
        msg = msg.decode()
        #print(repr(msg))
        
        if msg == '':
            #self.send(self.last)
            return

        if self.partial_msg:
            msg = self.partial_msg + msg
        
        msg = msg.split('\n')
        if msg[-1] == '':
            self.partial_msg = None
            msg.pop(-1)
        else:
            self.partial_msg = msg.pop(-1)

        for m in msg:
            if self.last == 'name' or self.last == 'taken':
                self.set_name(m)
            elif self.last == 'play':
                self.make_play(m)
            elif self.last in ['win', 'lose', 'disconnect']:
                self.play_again(m)

        return True

    def request_name(self):
        self.send('name')

    def set_name(self, msg):
        if len(msg) > 3 and mom.name_available(msg):
            self.name = msg
            print("{} has identified as {}.".format(self.socket.getpeername(), self.name))
            self.find_game()
        else:
            self.send('taken')

    def find_game(self):
        if mom.start_game(self):
            #self.send('opponent {}'.format(self.opponent))
            print("{} is starting a game with {}.".format(self.name, self.opponent.name))
        else:
            self.send('wait')

    def set_opponent(self, opponent):
        self.opponent = opponent
        self.send('opponent {}'.format(self.opponent.name))
        self.send('play')
        
    def make_play(self, play):
        if len(play) < 1 or play[0] not in 'rps':
            print("Invalid play from {}".format(self.name))
            self.send('play')
        else:
            self.play = play[0]
            oppo_play = self.opponent.play
            if oppo_play:
                if self.play == oppo_play:
                    self.tie()
                    self.opponent.tie()
                    
                elif mom.wins[self.play] == oppo_play:
                    self.opponent.lose()
                    self.win()
                else:
                    self.opponent.win()
                    self.lose()
                    
    def play_again(self, msg):
        if len(msg) < 1 or msg[0] not in 'yn':
            self.send(self.last)
        elif msg == 'y':
            self.find_game()
        else:
            self.socket.close()
            mom.remove_client(self.socket)
            
    def end_game(self):
        self.opponent = None
        self.send('disconnect')

    def win(self):
        self.send('win')
        self.play = None
        self.opponent = None

    def lose(self):
        self.send('lose')
        self.play = None
        self.opponent = None

    def tie(self):
        self.send('tie')
        self.play = None
        self.send('play')
