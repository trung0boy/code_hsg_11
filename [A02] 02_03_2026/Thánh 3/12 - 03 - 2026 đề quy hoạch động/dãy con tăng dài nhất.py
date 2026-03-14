import sys
import bisect

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))


#c1
dp = [1]*(n+1)
for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))

#c2
parent =[]
for x in A:
    idx = bisect.bisect_left(A,x)
    if idx == len(parent):
        parent.append(x)
    else:
        parent[idx] = x
print(parent)
