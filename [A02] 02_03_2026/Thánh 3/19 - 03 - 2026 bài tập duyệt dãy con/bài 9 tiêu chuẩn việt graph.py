import sys
from collections import Counter
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

A = sorted(Counter(A).items())
ans = 0
cnt = 0
for x in A:
    if x[1] > cnt :
        ans = x[0]
        cnt = x[1]
print(ans)

