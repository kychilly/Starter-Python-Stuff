import random

def trial(n=100):
    seats = [None]*(n+1)

    # assuming we r like super unlucky and the first passenger is the crazy one...
    first = random.randint(1,n)
    seats[first] = 1

    for p in range(2,n+1):
        if seats[p] is None:
            seats[p] = p
        else:
            empty = [i for i in range(1,n+1) if seats[i] is None]
            seats[random.choice(empty)] = p

    return seats[n] == n


def simulate(trials=100000):
    wins = sum(trial() for _ in range(trials))
    return wins / trials

print(simulate())