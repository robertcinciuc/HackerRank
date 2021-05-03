#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def binarySearch(myList, startIndex, elem):

    res = -1
    if(len(myList) == 1 ):
        if(myList[0] > elem):
            return startIndex + 1
        else:
            return startIndex

    else:

        if( myList[math.trunc(len(myList)/2)] == elem ):
            return startIndex + math.trunc(len(myList)/2)
        
        elif( myList[math.trunc(len(myList)/2)] > elem ):
            
            # Fill new list with second half of initial list
            newList = [] 
            for index in range(math.trunc(len(myList)/2), len(myList)):
                newList.append(myList[index])

            res = binarySearch(newList, math.trunc(len(myList)/2) + startIndex, elem )
        
        else:

            # Fill new list with first half of initial list
            newList = []
            for index in range(math.trunc(len(myList)/2)):
                newList.append(myList[index])   
            
            res = binarySearch(newList, startIndex, elem )

    return res


def climbingLeaderboard(ranked, player):

    # Build a lsit of [rankValue, numberOfPresentTimes]
    rankedCount = []
    for index in range(len(ranked)):
        if( len(rankedCount) > 0 ):
            if(rankedCount[len(rankedCount)-1][0] == ranked[index]):
                rankedCount[len(rankedCount) - 1][1] += 1
            else:
                rankedCount.append([ranked[index], 1])
        else:
            rankedCount.append([ranked[index], 1])
    
    res = []

    # Get just the scores
    rankedScores = []
    for index in range(len(rankedCount)):
        rankedScores.append(rankedCount[index][0])

    #Get the order of each score
    newRanking = rankedScores.copy()
    pos = 0
    lastPos = len(rankedScores)
    for i in range(len(player)):
        print("i=" + str(i))
        # Method 1:  with shortening the ranked list
        # if( pos > 0 ):
        #     newRanking = []
        #     for j in range(pos - 1):
        #         newRanking.append(rankedScores[j])
        # pos = binarySearch(newRanking, 1, int(player[i]))
        
        # Method 2: classic - iterating through all the list 
        # pos = binarySearch(rankedScores, 1, int(player[i]))

        # Method 3: iterate from low to high score, starting from last position
        found = True
        for j in reversed(range(0,lastPos)):
            
            print(j)
            if(player[i] == rankedCount[j][0]):
                pos = j+1
                found = True
                break

            elif( player[i] < rankedCount[j][0] and j < len(rankedCount) - 1 and rankedCount[j+1][0] < player[i]):
                pos = j+2
                found = True
                break

            elif( j == 0 and player[i] > rankedCount[j][0]):
                pos = 1
                found = True
                break

            elif( player[i] < rankedCount[j][0] and j == len(rankedCount) - 1):
                pos = len(rankedCount) + 1
                found = True
                break
        
        if( not found ):
            pos = lastPos
            print("not found " + str(pos))
        
        lastPos = pos - 1

        res.append(pos)

    return res

if __name__ == '__main__':

    # myList = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    # index = binarySearch(myList, 1, 35)
    # print("index=" + str(index))

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    
    print(result)
