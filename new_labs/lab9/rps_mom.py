from rps_user import User

wins = {'r' : 's', 's' : 'p', 'p' : 'r'}
inputs = []
users = {}
waiting = []

def add_client(client):
    users[client] = User(client)
    inputs.append(client)

def remove_client(client):
    if users[client].opponent:
        users[client].opponent.end_game()
    del users[client]
    inputs.remove(client)

def name_available(name):
    for u in users:
        if name == users[u].name:
            return False
    return True

def start_game(seeker):
    if waiting:
        player = waiting.pop(0)
        player.set_opponent(seeker)
        seeker.set_opponent(player)
        return True
    else:
        waiting.append(seeker)
        return False
