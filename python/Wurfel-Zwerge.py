#!/usr/bin/env python3

numColors = 6
numDice = 3
numSections = numDice


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def multichoose(n, k):
    return choose(n + k - 1, k)


if "__main__" == __name__:
    # if the dice had sections (top, middle, bottom)
    print("permutations with repetition = k ** n")
    print("with sections: {}".format(numColors**numDice))
    # the dice have no sections (top, middle, bottom)
    print("k-combinations with repetition = n multichoose k")
    print(
        "without sections and with repetitions: {}".format(
            multichoose(numColors, numDice)
        )
    )
    # no repetitions
    print("k-combinations without repetitition = n choose k")
    print(
        "without sections and without repetition: {}".format(choose(numColors, numDice))
    )
