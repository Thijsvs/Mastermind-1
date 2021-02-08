import random

# variable voor keuze eigen code of random generated
# waarde 0 = user
# waarde 1 = RNG
howtocode = int(input("Code zelf maken of laten genereren? 0=user input,  1=RNG"))
if howtocode ==0:
    TempList = [input('vul 4 cijfers in( 1 t/m 6')]
    print(usercode)
elif howtocode ==1:
    TempList = [list(map(int, random.sample(range(0, 6), 4)))]
    print(TempList)



# variable die aangeeft welk algoritme gebruikt word
# waarde 0 = user input
# waarde 1 = knutz
algorithm = int(input("Welk algorithme wil je gebruiken?0 = user input, 1 = Knutz"))




# returns how many bulls and cows
def HowManyBc(guess, secret):
    invalid = max(guess) + 1
    bulls = 0
    cows = 0
    r = 0
    while r < 4:
        if guess[r] == secret[r]:
            bulls = bulls + 1
            secret[r] = invalid
            guess[r] = invalid
        r = r + 1
    r = 0
    while r < 4:
        p = 0
        while p < 4:
            if guess[r] == secret[p] and guess[r] != invalid:
                cows = cows + 1
                secret[p] = invalid
                break
            p = p + 1
        r = r + 1
    return [bulls, cows]


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


while algorithm==1:
    # Maakt een list in een list. Deze list bevat 4 strings met characters 0 tot 5
    #TempList = [list(map(int, random.sample(range(6), 4)))]

    for secret in TempList:
        guess = [0, 0, 1, 1]
        BC = HowManyBc(guess, secret)
        counter = 1
        optionList = []
        allList = []
        for i0 in range(0, 6):
            for i1 in range(0, 6):
                for i2 in range(0, 6):
                    for i3 in range(0, 6):
                        optionList.append([i0, i1, i2, i3])
                        allList.append([i0, i1, i2, i3])
        while len(optionList) > 1:
            dummyList = []
            for i0 in range(0, 6):
                for i1 in range(0, 6):
                    for i2 in range(0, 6):
                        for i3 in range(0, 6):
                            opSecret = [i0, i1, i2, i3]
                            if HowManyBc(guess[:], opSecret[:]) == BC:
                                dummyList.append(opSecret)
            List1 = [item for item in optionList if item in dummyList]
            optionList = List1[:]
            nextGuess1 = []
            item1Max = 0
            L2 = optionList[:]
            L1 = allList[:]
            for item1 in L1:
                ListBC = []
                for item2 in L2:
                    ListBC.append(HowManyBc(item1[:], item2[:]))
                HMList = [0] * 14
                for BC1 in ListBC:
                    index = Adjustment(BC1)
                    HMList[index] = HMList[index] + 1
                # m=MinimumNozeros(HMList[:])
                m = len(L1) - max(HMList[:])
                if m > item1Max:
                    item1Max = m
                    nextGuess1 = item1[:]
            guess = nextGuess1[:]
            BC = HowManyBc(guess[:], secret[:])
            counter = counter + 1

    print(TempList)
    print(counter)
