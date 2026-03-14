import sys
sys.stdin = open('đường đi trên lưới có tổng nhỏ nhât.txt','r')
input = sys.stdin.readline

n,m = map(int,sys.stdin.readline().split())

A =[[0]*(n+1)]
for i in range(n):
    a=[0] + list(map(int,sys.stdin.readline().split()))
    A.append(a)

dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==1 and j == 1:
            dp[i][j] = A[i][j]
        if i == 1:
            dp[i][j] = dp[i][j-1] + A[i][j]
        elif j == 1:
            dp[i][j] = dp[i-1][j] + A[i][j]
        else:
            dp[i][j] = min(dp[i][j-1] + A[i][j] , dp[i-1][j] + A[i][j])
            
print(dp[n][m])
