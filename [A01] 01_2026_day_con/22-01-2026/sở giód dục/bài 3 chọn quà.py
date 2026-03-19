import sys
sys.stdin = open('bài 3 chọn quà.txt','r')

n,m = map(int,sys.stdin.readline().split())
V = [0]
W = [0]
for _ in range(n):
    vi,wi = map(int,sys.stdin.readline().split())
    W.append(wi)
    V.append(vi)

dp =[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j]
        if j >= W[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - W[i]] + V[i])
print(dp[n][m])
