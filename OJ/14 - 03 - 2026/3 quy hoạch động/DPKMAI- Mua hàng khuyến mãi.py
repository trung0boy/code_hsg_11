import sys
#sys.stdin = open('DPKMAI.txt','r')
#input = sys.stdin.readline

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))


dp = [[float('inf')]*(n+1) for i in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    for j in range(n):
        c = dp[i-1][j]
        if c == float('inf'):
            continue
        if j > 0:
            dp[i][j-1] = min(dp[i][j-1],c)
        if A[i-1]>100:
            g = 1
        else:
            g = 0
        if (j+g) <= n:
            dp[i][j+g] = min(dp[i][j+g], c+A[i-1])
print(min(dp[-1]))
