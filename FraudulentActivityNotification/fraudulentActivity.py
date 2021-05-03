#!/bin/python3

import math
import os
import random
import re
import sys

# # Complete the activityNotifications function below.
# def activityNotifications(expenditure, d):

#     expCopySort = []
#     count = 0
#     pos = []
#     for i in range(len(expenditure)):

#         if(i >= d):
            
#             posCurr = pos.pop(0)

#             print(expCopySort)

#             if(d % 2 == 0):
#                 med = 0.5 * expCopySort[math.trunc(d/2) - 1] + 0.5 * expCopySort[math.trunc(d/2)]
#             else:
#                 med = expCopySort[math.trunc(d/2)]
            
#             if( expenditure[i] >= med *2):
#                 count += 1
#                 print("med=" + str(med))
#                 print("count=" + str(count))

#             elem = expenditure[i]
#             newPos = 0

#             if( elem == expCopySort[posCurr]):
#                 continue
            
#             elif( elem > expCopySort[posCurr]):
#                 newPos = len(expCopySort) - 1
#                 # Find the correct place for the new element
#                 for j in range(posCurr, len(expCopySort)):
#                     if( elem < expCopySort[j]):
#                         newPos = j - 1
#                         break
#                     elif( elem == expCopySort[j]):
#                         newPos = j
#                         break
                
#                 # Shift all elements between pos and newpos to the left
#                 for j in range(posCurr, newPos):
#                     expCopySort[j] = expCopySort[j+1]
            
#             elif( elem < expCopySort[posCurr]):
#                 # Find the correct place for the new element
#                 for j in reversed(range(posCurr)):
#                     if( elem > expCopySort[j]):
#                         newPos = j + 1
#                         break
#                     elif( elem == expCopySort[j]):
#                         newPos = j
#                         break
                
#                 # Shift all elements between pos and newpos to the right
#                 for j in range(newPos, posCurr):
#                     expCopySort[j] = expCopySort[j-1]
            
#             expCopySort[newPos] = elem
#             pos.append(newPos)
        
#         else:
#             expCopySort.append(expenditure[i])
#             tmp = expCopySort.copy()
#             expCopySort = sorted(tmp)
            
#             for j in range(len(expCopySort)):
#                 if(expCopySort[j] == expenditure[i]):
#                     pos.append(j)
#                     break
            
#     return count

def activityNotifications(expenditure, d):

    count = 0
    segm = []
    countList = [0] * 201
    
    for i in range(len(expenditure)):
        if( i >= d ):
            
            # Find median
            med = 0
            if(d % 2 == 0):
                a, b = 0, 0
                countTmp = 0
                for j in range(len(countList)):
                    countTmp += countList[j]
                    if(countTmp >= int(d/2)):
                        a = j
                        break
                countTmp = 0
                for j in range(len(countList)):
                    countTmp += countList[j]
                    if(countTmp >= int(d/2) + 1):
                        b = j
                        break
                med = (a + b)/2

            else:
                countTmp = 0
                for j in range(len(countList)):
                    countTmp += countList[j]
                    if(countTmp >= int(d/2) + 1):
                        med = j
                        break
                
            if( expenditure[i] >= med * 2):
                count += 1
            
            # Updating segm and count list
            tmp = segm.pop(0)
            segm.append(expenditure[i])

            countList[tmp] -= 1
            countList[expenditure[i]] += 1

        else:
            segm.append(expenditure[i])
            countList[expenditure[i]] += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
