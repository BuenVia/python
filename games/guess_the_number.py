#Import Random module
import random
#Create random number using ranndint and assign to variable
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")


#For loop that runs for 6 guesses (range) or breaks if guess is correct
for guessesTaken in range(1, 7):
    print("Take a guess")
#The variable for the user's guess
    guess = int(input())

#IF statement inside of For loop. If guess is too low.
    if guess < secretNumber:
        print("Your guess is too low")
#IF guess is too high.
    elif guess > secretNumber:
        print("Your guess is too high")
#IF guess matches secretNumber OR user has attempted 6 times, the for loop breaks and exits to next stage.
    else:
        break

#Once user has guessed or used 6 attempts
#IF guess correct:
if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
#IF user attempted 6 times
else:
    print("Nope! The number I was thinking of was: " + str(secretNumber))