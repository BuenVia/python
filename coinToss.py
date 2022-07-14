import random

flip = random.randint(1,2)

def coinToss(x):
    if x == 1:
        print("Heads")
    elif x == 2:
        print("Tails")
            
coinToss(flip)
