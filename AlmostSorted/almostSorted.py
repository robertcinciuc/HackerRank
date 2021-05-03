#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):

    # Part to see if array ascending
    found = False
    index = 0
    for i in range(len(arr)):
        if(i < len(arr) - 1 and arr[i] > arr[i+1]):
            found = True
            index = i
    
    if(found == True):
        print("found=" + str(found))
        print("index=" + str(index))
        print("arr[i]=" + str(arr[i]))
        print("arr[i+1]" + str(arr[i+1]))
    else:
        print("not found")

    # # Part with swap
    # arrSorted = sorted(arr)

    # i = 0
    # j = 0
    # count = 0
    # found = False
    # start = 0
    # end = 0
    # while(i < len(arr) and j < len(arrSorted)):

    #     if( not arr[i] == arrSorted[j] ):
    #         count += 1

    #         if(found == False):
    #             found = True
    #             start = i

    #         elif(count == 2):
    #             end = i

    #     i += 1
    #     j += 1

    # s = ""
    # if(count == 2 and found == True):
    #     s += "yes\n"
    #     s += "swap " + str(start+1) + " " + str(end+1) + "\n"
    #     return s
    # elif(count == 0):
    #     return "yes"

    # # Part with reverse
    # start = 0
    # end = 0
    # found = False
    # inside = False
    # s = ""
    # for i in range(len(arr)):
    #     if(i < len(arr) -1 and arr[i] > arr[i+1]):
    #         if(found == False and inside == False):
    #             found = True
    #             start = i
    #             inside = True
    #         elif( inside == False and found == True):
    #             print("inside=" + str(inside))
    #             print(i)
    #             return "no1\n"
        
    #     if( i < len(arr) - 1 and arr[i] < arr[i+1] and found == True and inside == True):
    #         end = i
    #         inside = False
    
    # if(found == True and inside == True):
    #     end = len(arr) - 1

    # # if(found == False and start == 0 and end == 0):
    # #     return "yes\n"

    # if(found == True):
    #     if( end < len(arr) - 1 and start > 0 and arr[start-1] <= arr[end] and arr[end+1] >= arr[start] ):
    #         s += "yes\n"
    #         s += "reverse " + str(start+1) + " " + str(end+1) + "\n"
    #         return s
    #     elif(start > 0 and arr[start-1] <= arr[end]):
    #         s += "yes\n"
    #         s += "reverse " + str(start+1) + " " + str(end+1) + "\n"
    #         return s
    #     elif(end < len(arr) - 1 and arr[end+1] >= arr[start]):
    #         s += "yes\n"
    #         s += "reverse " + str(start+1) + " " + str(end+1) + "\n"
    #         return s
    #     elif( end - start + 1 == len(arr)):
    #         s += "yes\n"
    #         s += "reverse " + str(start+1) + " " + str(end+1) + "\n"
    #         return s
            
    
    # # print("start="+str(start))
    # # print("end="+str(end))

    # # return s
    return "no"


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = almostSorted(arr)

    print(res)
