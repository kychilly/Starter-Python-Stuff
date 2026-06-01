import math
import random

def solveProblem():
    for i in range(10):
        for p in range(10):
            test = int(str(i)+str(p)+str(p)+str(p)+str(i))
            if test%36 == 0:
                print(i + p)

solveProblem()

def solveSecondProblem():
    workingNumbers = []
    for i in range(50):
        if i**i % 5 == 0:
            workingNumbers.append(i)
    #print(workingNumbers)

solveSecondProblem()

def solveThirdProblem() -> int:
    n = 0
    for i in range(2,10):
        for p in range(2,10):
            for f in range(2,10):
                if .99 < (1.0/i + 1.0/p + 1.0/f):
                    if 1.01 > (1.0/i + 1.0/p + 1.0/f):
                        n += 1


    return n

#print(solveThirdProblem())

def solveFourthProblem() -> float:
    n = 0
    gender = [0,0]
    listy = []
    for i in range(20):
        if random.randint(0,1) == 0:
            listy.append(True)
            gender[0] += 1
        else:
            listy.append(False)
            gender[1] += 1
    while gender[0] != 0 and gender[1] != 0:
        n += 1
        if listy.pop(0):
            gender[0] -= 1
        else:
            gender[1] -= 1
        if random.randint(0,1) == 0:
            listy.append(True)
            gender[0] += 1
        else:
            listy.append(False)
            gender[1] += 1

    return n

#print(solveFourthProblem())

def solveFifthProblem() -> float:
    sum = 0
    for i in range(2,10):
        sum += math.pow(i+1,2) - math.pow(i,2)
        i += 1
    return sum

#print(solveFifthProblem())

#/*
    # //Roger abhors doing his homework. He starts with 3 questions to do, denoted c = 3,
    # //and he finishes when c = 0. However, he also starts with a spite value of s = 1.
    # //Given s, the probability of him getting his next question correct is 2 / (s + 2).
    # //If he gets it right, c decreases by 1. If not, his spite increases by 1, and he hates
    # //the world just a little bit more. On average, how many attempts will it take for him
    # //to complete the homework?
    # //
    # //Question taken from the Gunn Math Competition.
    # */
    # //make trials 1000
def solveSixthProblem(c = int) -> int:
    attempts = 0
    spite = 1
    while c > 0:
        attempts += 1
        if random.random() < (2/(spite+2)):
            c -= 1
        else:
            spite += 1
    return attempts

def simulateSixthProblem(c: int, trials: int) -> float:
    attempts = 0
    for i in range(trials):
        attempts += solveSixthProblem(c)
    return attempts/trials

#print(simulateSixthProblem(3,1000))

def simulateSeventhProblem(n: int):
    times = 0
    listy = []
    for i in range(n):
        listy.append(False)
    while True:
        times += 1
        rand = random.randint(0,n-1)
        listy[rand] = True
        works = True
        for i in range(0,n):
            if listy[i] == False:
                works = False
        if (works == True):
            return times
#print(simulateSeventhProblem(10))

# average proportion to go 6-7 in valorant
def simulateEigthProblem(trials : int) -> float:
    SixSevens = 0
    NotSixSevens = 0
    for p in range(trials):
        listy = [0,0]
        for i in range(13):
            if random.random() <= .5:
                listy[0] += 1
            else:
                listy[1] += 1
        if listy[0] == 6 and listy[1] == 7:
            SixSevens += 1
        else:
            NotSixSevens += 1
    return (SixSevens/(SixSevens+NotSixSevens))

#print (simulateEigthProblem(100000))

def simulateChipProblem() -> float:
    successes = 0
    for i in range (1,1000):
        chips = 2000
        bets = 0
        while chips > 0 and bets < 10000:
            if random.random() < .6:
                chips -= 1
            else:
                chips += 1
            bets += 1
        if bets == 10000: successes += 1
        else: successes += 0
    return (successes/1000)
print(simulateChipProblem())