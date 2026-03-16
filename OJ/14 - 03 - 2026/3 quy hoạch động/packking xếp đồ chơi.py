import sys
#sys.stdin = open('packking xếp đồ chơi.txt','r')
#input = sys.stdin.readline

n,V = map(int,sys.stdin.readline().split())
A = [0] + list(map(int,sys.stdin.readline().split()))

dp = [[0]*(V+1) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,V+1):
        dp[i][j] = dp[i-1][j]
        
        if j >= A[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - A[i]] + A[i])
print(dp[n][V])
