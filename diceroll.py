import random


def roll():

    rolls = []

    for i in range(0,4):
        rolls.append(random.randint(1, 6))

    rolls.sort()
    print rolls
    total = rolls[1] + rolls[2] + rolls[3]
    return total

def rollOver10():
    attribute = roll()
    while (attribute <= 10):
        attribute = roll()
    print attribute
    return attribute

def rollAllAttributes():
    for i in range(0, 6):
        rollOver10()

#rollOver10()
rollAllAttributes()
