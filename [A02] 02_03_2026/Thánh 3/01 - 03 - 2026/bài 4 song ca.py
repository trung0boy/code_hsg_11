import sys
from collections import * # deque, Counter,....
import math

sys.set_int_max_str_digits(10**9)
n = int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

A=Counter(A) # băm

ans = 0
for val in A:
    if A[val] > 1:
        ans += ((A[val] * ( A[val] - 1 ))//2)
print(ans)
        
