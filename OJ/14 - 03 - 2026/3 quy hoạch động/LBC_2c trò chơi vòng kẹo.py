import sys

n,m = map(int,sys.stdin.readline().split())
dp = [0]*(n+1)

for _ in range(m):
    l,r = map(int,sys.stdin.readline().split())
    l-=1
    r-=1
    if l > r:
        dp[0] += 1
    dp[l]+=1
    dp[r+1] -=1
curr = 0
ans = 0
for i in range(n):
    if ans == m:
        break
    curr += dp[i]
    ans = max(ans,curr)
print(ans)
