#!/usr/bin/python

# bibliography:
# http://www.codesandciphers.co.uk/enigma/steckercount.htm

numSlots = 3
numRotors = 5
alphabetSize = 26
numPairs = 10

def factorial(n):
    retValue = 1
    for i in range(2, n + 1):
        retValue *= i
    return(retValue)

# n = number of elements (possible choices)
# k = size of set (slots to hold the choices)
# n >= k
def permuteNoRepetition(n, k):
    assert n >= k
    return(factorial(n)/(factorial(n-k)))

def permuteWithRepetition(n, k):
    assert n >= k
    return(n**k)

def combination(n, k):
    assert n >= k
    return(factorial(n)/((factorial(n-k)*factorial(k))))

def plugBoard(n, k):
    assert n >= k
    retValue = 1
    for _ in range(k):
#       a, b is the same pair as b, a
        retValue *= combination(n, 2)
#       count by 2's as you pair off
        n -= 2
#   eliminate permutations of the same pairs
    retValue /= factorial(k)
    return(retValue)

print(('{} ways to arrange {} rotors in {} slots'.format(permuteNoRepetition(numRotors, numSlots), numRotors, numSlots)))
print(('{} ways to arrange {} letters in {} slots'.format(permuteWithRepetition(alphabetSize, numSlots), alphabetSize, numSlots)))
print(('{} ways to arrange {} wires in {} slots'.format(plugBoard(alphabetSize, numPairs), numPairs, alphabetSize)))
print(('{} possible keys'.format(permuteNoRepetition(numRotors, numSlots) * permuteWithRepetition(alphabetSize, numSlots) * plugBoard(alphabetSize, numPairs))))
print(('{:E}'.format(permuteNoRepetition(numRotors, numSlots) * permuteWithRepetition(alphabetSize, numSlots) * plugBoard(alphabetSize, numPairs))))
print(('{}: direct calculation'.format((13*25)*(12*23)*(11*21)*(10*19)*(9*17)*(8*15)*(7*13)*(6*11)*(5*9)*(4*7)*(26**3)*60/(10*9*8*7*6*5*4*3*2))))
print(('{:E}: direct calculation'.format((13*25)*(12*23)*(11*21)*(10*19)*(9*17)*(8*15)*(7*13)*(6*11)*(5*9)*(4*7)*(26**3)*60/(10*9*8*7*6*5*4*3*2))))
