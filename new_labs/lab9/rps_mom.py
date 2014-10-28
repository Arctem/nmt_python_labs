from rps_user import User

wins = {'r' : 's', 's' : 'p', 'p' : 'r'}
inputs = []
users = {}
waiting = []

def add_client(client):
    users[client] = User(client)
    inputs.append(client)

def remove_client(client):
    if users[client] in waiting:
        waiting.remove(users[client])
    if users[client].opponent:
        users[client].opponent.end_game()
    del users[client]
    inputs.remove(client)

def get_names():
    return list(map(lambda u: users[u].name, users))

def name_available(name):
    return name not in get_names()

def start_game(seeker):
    if waiting:
        player = waiting.pop(0)
        player.set_opponent(seeker)
        seeker.set_opponent(player)
        return True
    else:
        waiting.append(seeker)
        return False
