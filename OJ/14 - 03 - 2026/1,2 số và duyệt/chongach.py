import sys
#sys.stdin = open('chongach.txt','r')
#input = sys.stdin.readline

n = int(sys.stdin.readline())
#A = list(map(sys.stdin.readline().split()))
A=[]
for i in range(n):
    x = int(sys.stdin.readline())
    A.append(x)
A.sort()

leght = 1# cao nhất
limit = A[-1]-1 # giới hạn
for i in range(n-1,-1,-1):
    if limit <1:
        break
    if A[i] < limit:
        limit = A[i]
    limit -= 1
    leght += 1
print(leght)

'''

Test case #1:	AC	[0,023s,	11,13 MB]	(1/1)
Test case #2:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #3:	WA	[0,022s,	11,25 MB]	(0/1)
Test case #4:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #5:	WA	[0,061s,	15,00 MB]	(0/1)
Test case #6:	WA	[0,050s,	15,25 MB]	(0/1)
Test case #7:	WA	[0,022s,	11,00 MB]	(0/1)
'''
