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