import sys
import math
n = int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

A.sort

a = A[-1]
b =0

for i in range(len(A)-2,-1,-1): # vì số cuối cùng đã được cộng cho bạn a
    if a < b :
        a += A[i]
    else:
        b += A[i]
print( a + b + (abs(a-b)))
