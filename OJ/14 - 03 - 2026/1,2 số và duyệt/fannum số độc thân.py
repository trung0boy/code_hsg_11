import sys
from collections import Counter

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

B = Counter(A)
ans = 0
for x in B:
    if B[x] == 1:
        ans +=1
print(ans)



#full
