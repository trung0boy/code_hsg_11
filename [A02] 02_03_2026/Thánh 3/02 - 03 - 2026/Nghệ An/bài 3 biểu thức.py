import sys
import random
import time
from collections import *


def randomA(n):
    A=[]
    for i in range(n):
        A.append(random.randint(1,100))
    return A,"xong"
'''
n =100
A,x=randomA(n)
print(x)
'''
n,k = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

ans = a[0]

A = sorted(a[1::])

ans += sum(A[n-k-1::])
print(A[n-k-1::])
print(ans)


ans -= sum (A[:n-k-1])
print(A[:n-k-1])
print(ans)
