#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def lilysHomework(arr):

    countAsc = 0
    arrCopy = arr.copy()

    arrSortAsc = sorted(arr)
    arrSortDesc = sorted(arr, reverse=True)

    # Map with initial positions
    dicPos = {}
    for i in range(len(arr)):
        dicPos[arr[i]] = i
    
    dicPosCopy = dicPos.copy()

    # Main iteration
    for i in range(len(arrCopy)):

        if(not dicPos[arrSortAsc[i]] == i):
            tmpPos = dicPos[arrSortAsc[i]]
            dicPos[arrSortAsc[i]] = i
            dicPos[arrCopy[i]] = tmpPos

            tmp = arrCopy[i]
            arrCopy[i] = arrCopy[tmpPos]
            arrCopy[tmpPos] = tmp
            countAsc += 1
    
    countDesc = 0
    for i in range(len(arr)):

        maxi = -1
        pos = 0
        if(not dicPosCopy[arrSortDesc[i]] == i):
            tmpPos = dicPosCopy[arrSortDesc[i]]
            dicPosCopy[arrSortDesc[i]] = i
            dicPosCopy[arr[i]] = tmpPos

            tmp = arr[i]
            arr[i] = arr[tmpPos]
            arr[tmpPos] = tmp
            countDesc += 1
    
    if(countAsc < countDesc):
        return countAsc
    else:
        return countDesc


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
