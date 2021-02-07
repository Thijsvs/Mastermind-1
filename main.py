import random
import sys

#Variable voor lengte van secret code
width = 4

#variable die aangeeft welk algoritme gebruikt word
# waarde 0 = user input
# waarde 1 =
algorithm=0

def game(algorithm):
    hidden = list(map(str, random.sample(range(10), width)))
    print(f"Hidden numbers: {hidden}")
    turns = 0
    while turns < 9:
        if algorithm==0:
            inp = input("Guess a number: (e.g. 1234) or x to eXit. ")
        if inp == 'x' or inp == 'X':
            exit()
        guess = list(inp)
        turns += 1
        print(guess)
        result = []
        for ix in range(len(hidden)):
            if guess[ix] == hidden[ix]:
                result += '*'
            elif guess[ix] in hidden:
                result += '+'
            else:
                result += '-'
        print(result)
        if result == ['*'] * width:
            print(f'gratz!, je hebt {turns} poging(en) gebruikt.')
            break
        if turns > 8:
            print(f'Failed, je hebt { turns} pogingen gedaan.')
game(0)

#SOURCES
# https://code-maven.com/slides/python/solution-mastermind  voor de main game code