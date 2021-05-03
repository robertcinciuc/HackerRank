#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):

    res = []
    posCount = []
    if(k == 0):
        for i in range(1, n+1):
            res.append(str(i))
    
    else:
        if( not n%(k*2) == 0):
            res.append(str(-1))
        
        else:
            for i in range(1, n+1):
                
                if(i%(k*2) <= k and not i%(k*2) == 0):
                    res.append(i+k)
                else:
                    res.append(i-k)

    return res



if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
