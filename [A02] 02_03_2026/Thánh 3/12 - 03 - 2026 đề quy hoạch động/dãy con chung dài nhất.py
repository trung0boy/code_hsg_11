import sys
sys.stdin = open('dãy con chung dài nhất.txt','r')
input = sys.stdin.readline

n,m = map(int,sys.stdin.readline().split())
A = [0] + list(map(int,sys.stdin.readline().split()))
B = [0] +  list(map(int,sys.stdin.readline().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] =  max(dp[i-1][j], dp[i][j-1])
#print(dp)
print(dp[n][m])
