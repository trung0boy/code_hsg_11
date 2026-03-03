import sys
n,q = map(int,input().split())
A = list(map(int,input().split()))
Q = []
for i in range(q):
    l,r = map(int,input().split())
    #Q.append((l0-1,r0-1))

    b = sorted(A[l-1:r])
    n_b = len(b)
    print(
        b[((n_b+1)//2)-1]
        )
'''
for i in range(q):
    l = Q[i][0]
    r = Q[i][1]
    b = sorted(A[l:r+1])
    n_b = len(b)
    print(
        b[((n_b+1)//2)-1]
        )
'''
import math
math.cos

