"""
Alice purchased an array of  wooden boxes that she indexed from  to . On each box , she writes an integer that we'll refer to as .

Alice wants you to perform  operations on the array of boxes. Each operation is in one of the following forms:

(Note: For each type of operations, )

1 l r c: Add  to each . Note that  can be negative.
2 l r d: Replace each  with .
3 l r: Print the minimum value of any .
4 l r: Print the sum of all .
"""



#!/bin/python3

import math
import os
import random
import re
import sys
import math


def boxops(box, oplist):
    for op in oplist:
        if len(op)==4:
            num, l, r, a = op
            if num == 1:
                
                box = [item+a if ind in range(l, r+1) else item for ind, item in enumerate(box)]
                
            else:
                
                box = [math.floor(item/a) if ind in range(l,r+1) else item for ind, item in enumerate(box)]
                
        else:
            num, l, r = op
            if num == 3:
                print(min(box[l:r+1]))
                
            else:
                print(sum(box[l:r+1]))


if __name__ == '__main__':
    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    box = list(map(int, input().rstrip().split()))
    oplist = []
    for _ in range(q):
        oplist.append(list(map(int, input().strip().split())))
    boxops(box, oplist)

    # Write Your Code Here
