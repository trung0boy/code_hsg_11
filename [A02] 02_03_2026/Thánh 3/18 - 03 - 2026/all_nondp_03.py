import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())


pos = {0:1}
curr = 0
count = 0
for x in A:
    curr += x
    if curr - k in pos:
        count +=1
    pos[curr] = pos.get(curr,0) + 1
print(count)












'''

Test case #1:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #2:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #3:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #4:	AC	[0,023s,	11,00 MB]	(1/1)
Test case #5:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #6:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #7:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #8:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #9:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #10:	AC	[0,022s,	10,88 MB]	(1/1)
Test case #11:	WA	[0,024s,	12,13 MB]	(0/1)
Test case #12:	WA	[0,029s,	13,88 MB]	(0/1)
Test case #13:	WA	[0,032s,	15,35 MB]	(0/1)
Test case #14:	WA	[0,030s,	15,07 MB]	(0/1)
Test case #15:	WA	[0,029s,	13,47 MB]	(0/1)
Test case #16:	WA	[0,028s,	13,63 MB]	(0/1)
Test case #17:	WA	[0,029s,	13,63 MB]	(0/1)
Test case #18:	WA	[0,029s,	13,62 MB]	(0/1)
Test case #19:	WA	[0,028s,	13,00 MB]	(0/1)
Test case #20:	WA	[0,029s,	13,59 MB]	(0/1)

'''
