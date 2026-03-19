import sys
import math
from collections import *

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
A = list(Counter(A).items())
count = 0

for i in range(len(A)):
    for j in range(i+1, len(A)):
        if math.gcd(  A[i][0], A[j][0]  ) == 1:
            #print(A[i][0], A[j][0], A[i][1], A[j][1])
            count += A[i][1]*A[j][1]
print(count)


