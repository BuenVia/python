#Imports the random module and the sys module (so that we can close our program)
import random, sys

print("ROCK, PAPER, SCISSORS")

#Variables which contain the scores for the game
wins = 0
losses = 0
ties = 0

#Main game loop. It will loop until we call sys.exit(). It holds the overall match score.
while True:
#Shows the scores each round.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#Second loop, performs the actions for each game. It runs at the start of each game and allows us to choose our move or quit.
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        playerMove = input()
 #The code for closing the match
        if playerMove == "q":
            sys.exit()
#The code for playing a game. If chosen, it 'breaks' and then runs the rest of the code below.
        if playerMove == "r" or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s or q')

#Code for the player's move.
    if playerMove == "r":
        print("ROCK versus...")
    elif playerMove == "p":
        print("PAPER versus...")
    elif playerMove == "s":
        print("SCISSORS versus...")

#Code for the PC's move. 
#Variable for creating a random computer move.
    randomNumber = random.randint(1,3)
#IF statement to assign the random number to an actual move.
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")

#Code which decides if the player and machine have made the same or different moves, and what value each move has.
    if playerMove == computerMove:
        print("It's a tie!")
        ties += 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins += 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins += 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins += 1
    elif playerMove == "r"and computerMove == "p":
        print("You lose!")
        losses += 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        losses += 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose!")
        losses += 1