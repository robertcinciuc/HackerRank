#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):

    right = 0
    front = 0
    for i in range(len(A)):
        right += max(A[i])
    
    for j in range(len(A[0])):

        maxi = 0
        for i in range(len(A)):
            if(A[i][j] > maxi):
                maxi = A[i][j]
        
        front += maxi
    
    # Rows from left to right
    hidSurface = 0
    maxBefore = 0
    for i in range(len(A)):

        maxBefore = 0
        for j in range(len(A[0])):
            
            if(A[i][j] > maxBefore):
                maxBefore = A[i][j]
            else:

                foundBigAfter = False
                maxAfter = 0
                # Search for a higher block afterwards
                for k in range(j,len(A[0])):
                    if(A[i][k] > A[i][j]):
                        foundBigAfter = True
                        if(A[i][k] > maxAfter):
                            maxAfter = A[i][k]

                if(foundBigAfter == True and maxBefore > A[i][j] and j > 0 and A[i][j] < A[i][j-1]):
                    if( A[i][j-1] > maxAfter):
                        hidSurface += maxAfter - A[i][j]
                        # print("Row-first, maxAfter=" + str(maxAfter) + " A[i][j]=" + str(A[i][j]) + " diff="+ str(maxAfter - A[i][j]) + " hid="+str(hidSurface))
                    else:
                        hidSurface += A[i][j-1] - A[i][j]
                        # print("maxBefore="+ str(maxBefore) + " maxAfter=" + str(maxAfter))
                        # print("Row-second, A[i][j-1]=" + str(A[i][j-1]) + " A[i][j]=" + str(A[i][j]) + " diff="+ str(A[i][j-1] - A[i][j]) + " hid="+str(hidSurface))
    
    # Columns from top to bottom
    maxBefore = 0
    for j in range(len(A[0])):

        maxBefore = 0
        for i in range(len(A)):
            
            if(A[i][j] > maxBefore):
                maxBefore = A[i][j]
            else:

                foundBigAfter = False
                maxAfter = 0
                # Search for a higher block afterwards
                for k in range(i,len(A)):
                    if(A[k][j] > A[i][j]):
                        foundBigAfter = True
                        if(A[k][j] > maxAfter):
                            maxAfter = A[k][j]

                if(foundBigAfter == True and maxBefore > A[i][j] and i > 0 and A[i][j] < A[i-1][j]):
                    if( A[i-1][j] > maxAfter):
                        hidSurface += maxAfter - A[i][j]
                        # print("Col-first, maxAfter=" + str(maxAfter) + " A[i][j]=" + str(A[i][j]) + " diff="+ str(maxAfter - A[i][j]) + " hid="+str(hidSurface))
                    else:
                        hidSurface += A[i-1][j] - A[i][j]
                        # print("Col-second, A[i-1][j]=" + str(A[i-1][j]) + " A[i][j]=" + str(A[i][j]) + " diff="+ str(A[i-1][j] - A[i][j]) + " hid="+str(hidSurface))

    return 2*right + 2*front + 2*len(A)*len(A[0]) + 2*hidSurface
            

if __name__ == '__main__':

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)
    print(result)
