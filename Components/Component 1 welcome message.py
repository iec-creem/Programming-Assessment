#import library random
import random
#import random integer
from random import randint

#list of names used by BOT
bot_names = ("Madge", "Abigail", "Aaron", "Eli", "Wiley", "Marie",
             "Jamaal", "Grover", "Fredrick", "Barton")

num = randint(0,9)
name = (bot_names[num])
print(name)