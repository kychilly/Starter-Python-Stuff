def solveProblem():
    for i in range(10):
        for p in range(10):
            test = int(str(i)+str(p)+str(p)+str(p)+str(i))
            if test%36 == 0:
                print(i + p)

solveProblem()