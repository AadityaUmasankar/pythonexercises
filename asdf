import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high = []
    low = []
    temp1 = scores[0]
    temp2 = scores[0]
    high.append(scores[0])
    low.append(scores[0])
    for i in scores:
        if i > temp1:
            high.append(i)
            temp1 = i
        if i < temp2:
            low.append(i)
            temp2 = i
    temp3 = int(len(high)-1)
    temp4 = int(len(low)-1)
    print("{} {}".format(temp3,temp4))


n = int(input())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

fptr.write(' '.join(map(str, result)))
fptr.write('\n')

fptr.close()
