
from collections import Counter
import sys
import time
import random


def randomA(A):
    A=[]
    for i in range(n):
        A.append(random.randint(1,1000000000))
    #n1 = random.randint(1,n-5)
    return A


n =1000000
#n = int(sys.stdin.readline())
#A = list(map(int,sys.stdin.readline().split()))
A = randomA(n)
A = Counter(A)

count = 0
for x in A:
    if A[x] % 2 != 0:
        count += 1
print(count)
















