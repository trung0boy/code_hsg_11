import sys
import heapq
from collections import *



n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

ans = 0

pos = {}
for i in range(n):
    if A[i] not in  pos:
        idx_left = A.index(A[i])
        idx_right = n - 1 - A[::-1].index(A[i])
        ans = max(ans, sum(A[idx_left : idx_right+1]))
        #print(ans)
    pos[A[i]] = pos.get(A[i],0) + 1
print(ans)
    
    
