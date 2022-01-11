import random

#Code that creates a list of 100 'Heads' or 'Tails' values

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


h = result.count("H")
t = result.count("T")

high = max(h, t)

print(f"The coinflip returned {h} counts of 'Heads' and {t} counts of 'Tails")

if h > t:
    print(f"Heads returned the highest amount at {h}")
else:
    print(f"Tails returned the highest amount at {t}")

    #Code that checks if there is a streak of 6 heads or tails in a row.

