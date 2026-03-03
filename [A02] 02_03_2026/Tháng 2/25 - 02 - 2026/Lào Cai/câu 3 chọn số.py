import math
import sys
n,x = map(int,input().split())
A = list(map(int,input().split()))

if x <= n:
    for i in A:
        if n%2 == 0:
            count+=1
    comb = math.comb(count,x) #nCk
    print(comb)
    else:
        
