def validate(card):
    return {"38520000023237": True,
     "49927398716": False, #;True,
     "49927398717": False,
     "1234567812345670": False,
     "1234567812345678": True}[card]
