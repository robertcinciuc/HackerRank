#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    
    obsDict = defaultdict(list)
    res = 0

    # Put obstacles into a default dictionary : key = row; value = list of columns containing osbacle on that row
    for obstacle in obstacles:
        obsDict[obstacle[0]].append(obstacle[1])

    rowUp = r_q
    rowDown = r_q
    colLeft = c_q
    colRight = c_q
    directions = [1, 1, 1, 1, 1, 1, 1, 1] # starting from bottom left and going clockwise

    # Iterating starting from queen's position
    while(rowUp <= n or rowDown >= 1 or colLeft >= 1 or colRight <= n):
        
        # print('start for')
        for index in range(len(directions)):

            if(directions[index] == 1):

                # Choosing the right coordinates
                if(index == 0 or index == 1 or index == 2):
                    col = colLeft
                elif(index == 4 or index == 5 or index == 6):
                    col = colRight
                else:
                    col = c_q
                
                if(index == 0 or index == 7 or index == 6):
                    row = rowDown
                elif(index == 2 or index == 3 or index == 4):
                    row = rowUp
                else:
                    row = r_q

                # print("index=" + str(index) + " row=" + str(row) + " col=" + str(col))
                
                # Deciding whether to add 1 cell or not
                if( not(row == r_q and col == c_q) ):
                    if( len(obsDict[row]) == 0 and row <= n and row >= 1 and col >= 1 and col <= n):
                        res += 1
                        # print("index=" + str(index) + " row=" + str(row) + " col=" + str(col))

                    else:
                        found = False
                        for obsCol in obsDict[row]:
                            if(obsCol == col):
                                found = True
                        
                        if(found == True):
                            directions[index] = 0
                        elif(row <= n and row >= 1 and col >= 1 and col <= n):
                            res += 1
                            # print("index=" + str(index) + " row=" + str(row) + " col=" + str(col))
        
        rowUp += 1
        rowDown -= 1
        colLeft -= 1
        colRight += 1
    
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)


