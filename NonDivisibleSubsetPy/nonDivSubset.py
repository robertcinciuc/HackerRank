#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    
    res = 0

    if(k == 1):
        res = 1

    elif(k > 1):

        # Create lists of list of nb of the same remainder by diving k
        remaindersList = []
        for remainder in range(k):
            
            sameRemainder = []
            for elem in s:
                if(elem % k == remainder):
                    sameRemainder.append(elem)
            
            remaindersList.append(sameRemainder)
        
        # Add 1 element divisible by k
        if(len(remaindersList[0]) > 0 ):
            print('exactly divisible')
            res += 1
        
        # If k is pair, add 1 elem % k == k/2
        if( k % 2 == 0 and len(remaindersList[ int(k/2) ]) > 0 ):
            print('%2 == 0')
            res += 1
        
        # Take the longest list
        for remain in range(1, math.trunc(k/2) + 1):
            
            if( (k % 2 == 0 and remain != int(k/2)) or ( k % 2 == 1 ) ):
                if( len(remaindersList[remain]) >= len(remaindersList[k - remain]) ):
                    res += len(remaindersList[remain])
                
                else:
                    res += len(remaindersList[k - remain])
    
    return res


if __name__ == '__main__':

    for elem in range(1, 1):
        print(elem)

    # nbList = [19, 10, 12, 10, 24, 25, 22]
    nbList = [1, 7, 2, 4]
    # nbList = [13, 14, 16, 15, 23, 35, 22, 74, 42, 11, 12, 9]
    # nbList = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
    k = 3
    result = nonDivisibleSubset(k, nbList)

    print("res=" + str(result))
