import random

#Code that creates a list of 100 'Heads' or 'Tails' values
def coinFlip():
    flips = 0
    result = []
    while flips <= 10000:
        toss = random.randint(1,3)   
        if toss == 1:
            x = "H"
            flips += 1
            result += x
        elif toss == 2:
            y = "T"
            flips += 1
            result += y
    print(result)
    
coinFlip()


    #Code that checks if there is a streak of 6 heads or tails in a row.

