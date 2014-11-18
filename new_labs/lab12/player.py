class Player:
  def __init__(self, socket, name=None):
    self.socket = socket
    self.name = name

  #Returns False to indicate the connection should be terminated,
  #otherwise returns True.
  def handle_message(self, msg):
    if not msg:
      return False
    #Add custom handling code here.
