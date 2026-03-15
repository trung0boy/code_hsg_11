import sys
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

A.sort()

ans = float('inf')
for i in range(4,n):
    ans = min(ans,A[i] - A[i-4])
print(ans)

'''

Test case #1:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #2:	AC	[0,072s,	21,88 MB]	(1/1)
Test case #3:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #4:	AC	[0,022s,	10,88 MB]	(1/1)
Test case #5:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #6:	AC	[0,022s,	11,38 MB]	(1/1)
Test case #7:	AC	[0,031s,	13,10 MB]	(1/1)
Test case #8:	AC	[0,042s,	15,30 MB]	(1/1)
Test case #9:	AC	[0,051s,	17,18 MB]	(1/1)
Test case #10:	AC	[0,060s,	19,45 MB]	(1/1)
'''
