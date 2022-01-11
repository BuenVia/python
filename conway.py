import random, time, copy
WIDTH = 60
HEIGHT = 20

nextCells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(" ")
    nextCells.append(column)