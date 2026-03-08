import sys



n,m = map(int,input().split())
A=list(map(int,input().split()))

dp = [float('inf')]*(n+1)
dp[0]=0
for i in range(n+1):
    curr=0
    mx = 0
    for j in range(i,0,-1):
        curr += A[j-1]
        if curr > m:
            break
        mx = max(mx,A[j-1])
        dp[i] = min(dp[i], dp[j-1] + mx)
print(dp[n])
    
