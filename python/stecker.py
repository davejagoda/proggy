#!/usr/bin/python

# imagine an old-fashioned telco switchboard
# each socket is labelled with a letter from an alphabet
# you have a set of wires with a plug at each end
# numSockets is the total number of sockets available, and thus also the alphabetSize
# numWires is the number of wires, each of which has a plug on both ends

import itertools

def recursivePairPicker(remainingAlphabet, numWires, currentChain):
    if 0 == len(remainingAlphabet) or 0 == numWires:
#        print('remaining alphabet exhausted or out of wires, current chain: {}'.format(currentChain))
        pairSet = set()
        for pairElement in currentChain:
            pair = ''.join(sorted(pairElement))
            assert(pair not in pairSet)
            pairSet.add(pair)
        pairString = ''.join(sorted(pairSet))
        if pairString:
            setOfPairs.add(pairString)
        return(currentChain)
    for pairTuple in itertools.combinations(remainingAlphabet, 2):
        pair = ''.join(sorted(pairTuple))
        newChain = list(currentChain)
        newChain.append(sorted(pairTuple))
        recursivePairPicker(remainingAlphabet - set(pairTuple), numWires - 1, newChain)
    return(currentChain)

if '__main__' == __name__:
# in all cases numWires * 2 <= numSockets
    numWires = 0
    numSockets = 0
    maxSockets = 26
    socketNames = [chr(x+65) for x in range(maxSockets)]
#    print(socketNames)
    while numSockets <= maxSockets:
        while numWires * 2 <= numSockets:
            setOfPairs = set()
            print('numSockets: {} numWires: {} availableSockets: {}'.format(numSockets, numWires, socketNames[:numSockets]))
            recursivePairPicker(set(socketNames[:numSockets]), numWires, [])
            print('length of set: {} elements of set: {}'.format(len(setOfPairs), sorted(setOfPairs)))
            numWires += 1
        numSockets += 1
        numWires = 0
        print
