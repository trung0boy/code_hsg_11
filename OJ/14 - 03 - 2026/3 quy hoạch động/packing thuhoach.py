import sys
#sys.stdin = open('packing thuhoach.txt','r')
#input = sys.stdin.readline

n,M = map(int,sys.stdin.readline().split())
A = [0] + list(map(int,sys.stdin.readline().split()))

dp =[[0]*(M+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j]
        if j>=A[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i]] + A[i])
print(dp[n][M])

'''

Test case #1:	AC	[0,026s,	11,38 MB]	(1/1)
Test case #2:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #3:	AC	[0,217s,	22,00 MB]	(1/1)
Test case #4:	AC	[0,208s,	22,00 MB]	(1/1)
Test case #5:	AC	[0,177s,	18,63 MB]	(1/1)
Test case #6:	AC	[0,209s,	21,00 MB]	(1/1)
Test case #7:	AC	[0,234s,	22,63 MB]	(1/1)
Test case #8:	AC	[0,275s,	24,88 MB]	(1/1)
Test case #9:	AC	[0,308s,	26,63 MB]	(1/1)
Test case #10:	AC	[0,364s,	29,00 MB]	(1/1)
Test case #11:	AC	[0,023s,	11,25 MB]	(1/1)

'''
