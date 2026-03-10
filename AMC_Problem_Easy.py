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
    print(workingNumbers)

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

print(solveThirdProblem())

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

print(solveFourthProblem())

