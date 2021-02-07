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
    while True:
        if algorithm==0:
            inp = input("Guess a number: (e.g. 1234) or x to eXit. ")
        if inp == 'x' or inp == 'X':
            exit()
        guess = list(inp)
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
            print("SUCCESS")
            break
game()