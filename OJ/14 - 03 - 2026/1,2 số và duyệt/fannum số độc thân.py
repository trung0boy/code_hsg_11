import sys
from collections import Counter

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

B = Counter(A)
ans = 0
for x in B:
    if B[x] == 1:
        ans +=1
print(ans)



'''
Test case #1:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #2:	AC	[0,023s,	10,75 MB]	(1/1)
Test case #3:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #4:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #5:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #6:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #7:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #8:	AC	[0,023s,	11,13 MB]	(1/1)
Test case #9:	AC	[0,076s,	29,69 MB]	(1/1)
Test case #10:	AC	[0,310s,	116,73 MB]	(1/1)
'''
