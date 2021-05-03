#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):

    print("lenInsideFunc=" + str(len(s)))

    # for i in range(len(s)):
    #     print("i=" + str(i) + " s[i]=" + str(s[i]))
    
    # print("i=" + str(4095) + " s[i]=" + str(s[4095]))

    # # Count how many distinctions there are
    # count = 0
    # posValues = []
    # print("n=" + str(n))
    # print("int(n/2)=" + str(int(n/2)))
    # print("elem in middle=" + str(s[18000]))
    # for i in range(int(n/2)):
    #     if( not s[i] == s[n-i-1] ):
    #         count += 1
    #         posValues.append([i, s[i], s[i-1]])
    
    # if(count > k):
    #     return "-1"
    # else:
    #     if(len(posValues) > 0):

    #         j = 0
    #         while( k >= len(posValues) + 1 and k > 0 and len(posValues) > 0):

    #             print(posValues)
    #             print(k)

    #             if( not s[j] == '9' ):
    #                 k -= 1
    #                 s = s[:j] + '9' + s[j+1:]
    #             if( not s[n-j-1] == '9'):
    #                 k -= 1
    #                 s = s[:n-j-1] + '9' + s[n-j:]
                
    #             if( len(posValues) > 0 and posValues[0][0] == j):
    #                 posValues.pop(0)
                
    #             j += 1
            
    #         if(k > 0 and k > len(posValues) and not n % 2 == 0):
    #             k -= 1
    #             s = s[:int(n/2)] + '9' + s[int(n/2)+1:]

            
    #         for j in range(len(posValues)):

    #             print(s)

    #             if( posValues[j][1] > posValues[j][2] ):
    #                 s = s[:n - posValues[j][0] - 1] + s[posValues[j][0]] + s[n - posValues[j][0]:]
    #             elif( posValues[j][1] < posValues[j][2] ):
    #                 s = s[:posValues[j][0]] + s[n - posValues[j][0] - 1] + s[posValues[j][0] + 1:]
        
    #     else:
    #         j = 0 
    #         while(k > 0 and j <= n):
    #             print(j)
    #             if(n % 2 == 0):
    #                 if( not s[j] == '9' and k >= 2):
    #                     s = s[:n - j - 1] + '9' + s[n - j:]
    #                     s = s[:j] + '9' + s[j + 1:]
    #                     k -= 2
    #             else:
    #                 if( not s[j] == '9' and k >= 2 and not j == int(n/2) and not j == 0):
    #                     s = s[:n - j - 1] + '9' + s[n - j:]
    #                     s = s[:j] + '9' + s[j + 1:]
    #                     k -= 2
    #                     print('one')
    #                 elif( not s[j] == '9' and k >= 1 and (j == int(n/2) or (j == 0 and n == 1) )):
    #                     s = s[:j] + '9' + s[j + 1:]
    #                     k -= 1
    #                     print("two")
                
    #             j += 1


    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    # print("lenMain=" + str(len(s)))
    print(s)

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
