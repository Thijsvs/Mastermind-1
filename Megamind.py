# Bron 1: https://stackoverflow.com/questions/20302682/mastermind-in-python

import random
import time

def startgame():
    global Secretcode
    global algo_choice
    # variable voor keuze: eigen code of random generated
    # waarde 0 = user
    # waarde 1 = RNG
    howtocode = int(input("Code zelf maken of laten genereren?\n0=user input, 1=RNG"))

    #Gebruiker selecteerd optie: handmatige invoer van geheime code
    if howtocode ==0:
        #de input wordt eerst als string gemaakt, omdat bijvoorbeeld de code '0011'  als integer automatisch zou veranderen naar '11'
        Secretcode = [int(i) for i in [char for char in str(input('vul 4 cijfers in (0 t/m 5): '))]]
        print(f'Dit is de code dmv userinpit {Secretcode}')
    #Gebruiker selecteerd optie: random generated geheime code
    elif howtocode ==1:
        #hier word een list dat 4 willekeurige intergers bevat(0 tot 6) aangemaakt
        Secretcode = list(map(int, random.sample(range(0, 6), 4)))
        print(f'Dit is de code dmv random {Secretcode}')
    algo_choice = int(input("Welk algorithme wil je gebruiken?\n0=user input, 1=Knutz, 2=simple strategy"))
    selectalgo(algo_choice)


def selectalgo(algo_choice):
    # variable die aangeeft welk algoritme gebruikt word
    # waarde 0 = user input
    # waarde 1 = knutz
    # waarde 2 = simple strategy
    if algo_choice==0:
        breakit()
    if algo_choice==1:
        knutz(Secretcode)
    if algo_choice == 2:
        simplestrat(Secretcode)

#de gebruiker heeft gekozen om handmatig de code te kraken
def breakit():
    # de input wordt eerst als string gemaakt, omdat bijvoorbeeld de code '0011'  als integer automatisch zou veranderen naar '11'
    guess = [int(i) for i in [char for char in str(input('vul 4 cijfers in (0 t/m 5): '))]]
    print(f'Dit is de guess dmv userinput {guess}')
    print(pegs(guess, Secretcode, algo_choice))
    if pegs(guess, Secretcode, algo_choice) != [4,0]:
        breakit()
    else:
        print('GGWP')
        quit()

#deze functie returned een list met aantal red en white pegs.  Format:[red, white]
#inspired from 'bron 1'
def pegs(guess, Secretcode,algo_choice):
    red = 0
    white = 0
    for i in range(len(Secretcode)):
        if guess[i] == Secretcode[i]:
            red += 1
            continue
        if guess[i] in Secretcode and guess[i] != Secretcode[i]:
            white += 1
    return [red, white]

def pegstest(guess, Secretcode,algo_choice):
    red = 0
    white = 0
    tempcodecopy = Secretcode.copy()
    for i in range(0,len(tempcodecopy)):
        if guess[i] == tempcodecopy[i]:
            red += 1
            tempcodecopy[i]='rooie'
    for i in range(0,len(tempcodecopy)):
        if guess[i] in tempcodecopy and guess[i] != tempcodecopy[i]:
            white += 1
            tempcodecopy[i] = 'witte'

    return [red, white]

# sends every BC to its index in HMList
def Adjustment(BC1):
    if BC1 == [0, 0]:
        return 0
    elif BC1 == [0, 1]:
        return 1
    elif BC1 == [0, 2]:
        return 2
    elif BC1 == [0, 3]:
        return 3
    elif BC1 == [0, 4]:
        return 4
    elif BC1 == [1, 0]:
        return 5
    elif BC1 == [1, 1]:
        return 6
    elif BC1 == [1, 2]:
        return 7
    elif BC1 == [1, 3]:
        return 8
    elif BC1 == [2, 0]:
        return 9
    elif BC1 == [2, 1]:
        return 10
    elif BC1 == [2, 2]:
        return 11
    elif BC1 == [3, 0]:
        return 12
    elif BC1 == [4, 0]:
        return 13

# returns positive's list minimum without including zeros
def MinimumNozeros(List1):
    minimum = max(List1) + 1
    for item in List1:
        if item != 0 and item < minimum:
            minimum = item
    return minimum

def knutz(Secretcode):
        for secret in Secretcode:
            guess=[0,0,1,1]
            BC=HowManyBc(guess[:],secret[:])
            counter=1
            optionList=[]
            allList=[]
            for i0 in range(0,6):
                for i1 in range(0,6):
                    for i2 in range(0,6):
                        for i3 in range(0,6):
                            optionList.append([i0,i1,i2,i3])
                            allList.append([i0,i1,i2,i3])
            #while BC!=[4,0]:
            while len(optionList)>1:
                dummyList=[]
                for i0 in range(0,6):
                    for i1 in range(0,6):
                        for i2 in range(0,6):
                            for i3 in range(0,6):
                                opSecret=[i0,i1,i2,i3]
                                if HowManyBc(guess[:],opSecret[:])==BC:
                                    dummyList.append(opSecret)
                List1=[item for item in optionList if item in dummyList]
                optionList=List1[:]
                nextGuess1=[]
                item1Max=0
                #L1=optionList[:]
                #L2=allList[:]
                L2=optionList[:]
                L1=allList[:]
                for item1 in L1:
                    ListBC=[]
                    for item2 in L2:
                        ListBC.append(HowManyBc(item1[:],item2[:]))
                    HMList=[0]*14
                    for BC1 in ListBC:
                        index=Adjustment(BC1)
                        HMList[index]=HMList[index]+1
                    #m=MinimumNozeros(HMList[:])
                    m=len(L1)-max(HMList[:])
                    if m>item1Max:
                        item1Max=m
                        nextGuess1=item1[:]
                guess=nextGuess1[:]
                BC=HowManyBc(guess[:],secret[:])
                counter=counter+1
        print(Secretcode)
        print(counter)

#functie die de simpele strategie volgt
def simplestrat(Secretcode):
    count = 0
    alloption = []
    currentoption = []
    # Loop die alle mogelijk combinaties, in lists plaatst
    # De lists worden zo aangemaakt, dat ze gelijk gesorteerd zijn.
    for i0 in range(0, 6):
        for i1 in range(0, 6):
            for i2 in range(0, 6):
                for i3 in range(0, 6):
                    alloption.append([i0, i1, i2, i3])
                    currentoption.append([i0, i1, i2, i3])

    while True:
        #maak een gok met een willekeurige mogelijke optie
        guess = random.choice(currentoption)
        count += 1
        feedback = pegstest(guess, Secretcode,algo_choice)
        print(f'guess: {guess} feedback:{feedback}')

        if feedback == [4,0]:
            print(f'GGWP GAMER, het heeft {count} turns gekost')
            print(f'De code was {guess}.')
            quit()
        checklst=[]
        for i0 in range(0, 6):
            for i1 in range(0, 6):
                for i2 in range(0, 6):
                    for i3 in range(0, 6):
                        checksecret=[i0,i1,i2,i3]
                        print(f'result: { pegstest(guess, checksecret, algo_choice)}, checksecret : {checksecret}, guess: {guess}')

                        if pegstest(guess, checksecret, algo_choice)==feedback:
                            checklst.append(checksecret)
        currentoption =[item for item in currentoption if item in checklst]



startgame()
