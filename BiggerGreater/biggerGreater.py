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

def biggerIsGreater(w):

    w1 = w[:]
    swapped = False
    for i in reversed(range(len(w1))):

        if( i > 0 and w1[i] > w1[i-1]):
            
            mini = w1[i]
            pos = i
            print("i="+str(i))
            print("len(w1)="+str(len(w1)))
            for j in range(i, len(w1)):
                if( w1[j] > w1[i-1] and w1[j] < w1[i]):
                    mini = w1[j]
                    pos = j
                    print("found sth")

            w1 = w1[:pos] + w1[i-1] + w1[pos+1:]
            w1 = w1[:i-1] + mini + w1[i:]
            swapped = True

            # Sort the part to the right of i-1
            tmpArray = []
            for j in range(i, len(w1)):
                tmpArray.append(w1[j])
            
            w1 = w1[:i]
            sortedArray = sorted(tmpArray, reverse=True)

            for j in range(len(sortedArray)):
                w1 = w1 + sortedArray.pop()
            
            break
    
    if(swapped == True):
        return w1

    return 'no answer'


if __name__ == '__main__':

    T = int(input())

    response = []

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        response.append(result)
    
    print(response)
