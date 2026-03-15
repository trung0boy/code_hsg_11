import sys
#sys.stdin = open('thuhoach.txt','r')
#input = sys.stdin.readline

n,M = map(int,sys.stdin.readline().split())
A = [0] + list(map(int,sys.stdin.readline().split()))

dp =[[0]*(M+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i][j-1]
        if j>=A[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i]] + A[i])
print(dp[n][M])

'''

Test case #1:	AC	[0,025s,	11,50 MB]	(1/1)
Test case #2:	AC	[0,022s,	10,88 MB]	(1/1)
Test case #3:	AC	[0,212s,	22,13 MB]	(1/1)
Test case #4:	AC	[0,229s,	22,00 MB]	(1/1)
Test case #5:	AC	[0,193s,	18,88 MB]	(1/1)
Test case #6:	WA	[0,212s,	21,38 MB]	(0/1)
Test case #7:	WA	[0,240s,	24,25 MB]	(0/1)
Test case #8:	WA	[0,276s,	25,75 MB]	(0/1)
Test case #9:	WA	[0,299s,	26,88 MB]	(0/1)
Test case #10:	WA	[0,377s,	29,88 MB]	(0/1)
Test case #11:	AC	[0,022s,	11,13 MB]	(1/1)
'''
