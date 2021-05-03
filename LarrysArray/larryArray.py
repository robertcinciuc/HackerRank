#!/bin/python3

import math
import os
import random
import re
import sys

def shift2Left(myList, pos):

    newList = myList.copy()
    if(pos >= 2):
        tmp1 = newList[pos-2]
        tmp2 = newList[pos-1]
        newList[pos-2] = newList[pos]
        newList[pos-1] = tmp1
        newList[pos] = tmp2

    return newList

def shift1Left(myList, pos):

    newList = myList.copy()
    if(pos >= 1):
        tmp1 = newList[pos-1]
        newList[pos-1] = newList[pos]
        newList[pos] = newList[pos+1]
        newList[pos+1] = tmp1

    return newList

# Complete the larrysArray function below.
def larrysArray(A):

    lastSortedPos = 0
    newList = A.copy()
    for i in range(len(A)+1):

        # Get pos of the value i
        pos = 0
        for j in range(len(newList)):
            if(newList[j] == i):
                pos = j
        
        delta = abs(pos - i + 1)
        div = math.trunc(delta / 2)
        rest = delta % 2

        if( i == len(A) - 1 and div == 0 and rest > 0):
            return "NO"

        else:
            newPos = pos
            for k in range(div):
                newList = shift2Left(newList, newPos)
                newPos = newPos - 2
            
            if(rest>0):
                newList = shift1Left(newList, newPos)

            print(newList)
        

    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
