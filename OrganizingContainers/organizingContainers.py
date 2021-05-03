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

def organizingContainers(container):

    sumRow = []
    sumCol = []
    for rowIndex in range(len(container)):
        sumRow.append(sum(container[rowIndex]))
    
    for colIndex in range(len(container[0])):
        
        sumy = 0
        for rowIndex in range(len(container)):
            sumy += container[rowIndex][colIndex]
        
        sumCol.append(sumy)
    
    for i in range(len(sumRow)):

        rowEqualities = []
        for j in range(len(sumCol)):
            if(sumRow[i] == sumCol[j]):
                rowEqualities.append(1)
            else:
                rowEqualities.append(0)
        
        if(sum(rowEqualities) == 0):
            return 'Impossible'

    return 'Possible'


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)
