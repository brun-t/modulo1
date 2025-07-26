from random import shuffle
from string import ascii_letters

def password(length:int) -> str:
    data = list("@~.,+-/*!&$?=#" + ascii_letters + "ñ" + "0123456789")
    shuffle(data)
    return ''.join(data[0:length])
