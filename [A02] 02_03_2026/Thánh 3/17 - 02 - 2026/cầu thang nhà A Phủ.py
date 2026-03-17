import sys

n,k = map(int,sys.stdin.readline().split())
A = set(list(map(int,sys.stdin.readline().split())))

dp = [0]*(n+1)
dp[0] = 1

for i in range(1,n+1):
    if i in A:
        dp[i] = 0
    else:
        dp[i]=dp[i-1]
        if i >= 2:
            dp[i]+=dp[i-2]
print(dp[-1]%1000000007)
