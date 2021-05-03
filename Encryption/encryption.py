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

def encryption(s):

    floor = math.trunc(math.sqrt(len(s)))
    ceiling = floor

    if(floor * ceiling < len(s)):
        ceiling = floor + 1

        if(floor * ceiling < len(s)):
            floor += 1

    print(floor)
    print(ceiling)
    print(len(s))

    charMatrix = []
    count = 0
    for i in range(floor):

        row = []
        for j in range(ceiling):

            if(count >= len(s)):
                break
            else:
                row.append(s[count])
                count += 1
        
        charMatrix.append(row)

    res = ''
    for j in range(ceiling):

        for i in range(floor):
            if(j < len(charMatrix[i])):
                res += str(charMatrix[i][j])
        
        res += " "

    return res


if __name__ == '__main__':

    s = input()

    result = encryption(s)

    print(result)