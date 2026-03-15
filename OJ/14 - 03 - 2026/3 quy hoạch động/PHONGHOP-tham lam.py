import bisect
import sys
n = int(sys.stdin.readline())
A = []
for i in range(n):
    ai,bi = map(int,sys.stdin.readline().split())
    A.append((ai,bi,i+1))

A.sort(key = lambda x : x[1])

time_end = 0
dp = []
for s,e,i in A:
    if s >= time_end:
        time_end = e
        idx  = bisect.bisect(dp,i)
        dp.insert(idx,i)
        
print(*dp)

## chỉ lấy max
'''
dp = [1]*(n+1)

for i in range(n):
    for j in range(i):
        if A[i][0] >= A[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
'''

