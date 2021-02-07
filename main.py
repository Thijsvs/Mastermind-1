import random
import sys

width = 4

# TODO: verify that the user gave exactly width characters

def game():
    hidden = list(map(str, random.sample(range(10), width)))
    print(f"Hidden numbers: {hidden}")
    while True:
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