class Player:
  def __init__(self, socket, name=None):
    self.socket = socket
    self.name = name

  def handle_message(self, msg):
    if not msg:
      return False
    return True