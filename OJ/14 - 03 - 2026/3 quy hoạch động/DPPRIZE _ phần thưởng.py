import sys
#sys.stdin = open('DPPRIZE _ phần thưởng.txt','r')
#input = sys.stdin.readline



n,k = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))



# tổng dồn.
prefix =[0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + A[i]
#print(prefix)

# tổng cũa từng đoạn.
m = n-k+1
s = [0]*(m+1)
for i in  range(1,m+1):
    s[i] = prefix[i+k-1] - prefix[i-1]



    
# max đoạn từ trái sang phải
L = [0] * (m+1)
L[0] = s[0]
for i in range(1, m):
    L[i] = max(L[i-1], s[i])

# max đoạn từ phải sang trái
R = [0] * (m+2)
R[m-1] = s[m-1]
for i in range(m, -1, -1):
    R[i] = max(R[i+1], s[i])




res = float('inf')
for i in range(m):
    harry_can_get = 0
        
        
    if i - k >= 1:
        harry_can_get = max(harry_can_get, L[i - k])
    if i + k <= m:
        harry_can_get = max(harry_can_get, R[i + k])
            
    res = min(res, harry_can_get)

print(res)


'''
Test case #1:	AC	[0,024s,	11,12 MB]	(1/1)
Test case #2:	AC	[0,023s,	11,25 MB]	(1/1)
Test case #3:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #4:	AC	[0,022s,	11,38 MB]	(1/1)
Test case #5:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #6:	AC	[0,027s,	11,88 MB]	(1/1)
Test case #7:	AC	[0,028s,	12,00 MB]	(1/1)
Test case #8:	AC	[0,028s,	11,88 MB]	(1/1)
Test case #9:	AC	[0,029s,	12,00 MB]	(1/1)
Test case #10:	AC	[0,029s,	11,88 MB]	(1/1)
Test case #11:	AC	[0,029s,	12,00 MB]	(1/1)
Test case #12:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #13:	AC	[0,030s,	11,75 MB]	(1/1)
Test case #14:	WA	[0,029s,	11,88 MB]	(0/1)
Test case #15:	AC	[0,026s,	11,75 MB]	(1/1)
Test case #16:	AC	[0,026s,	11,63 MB]	(1/1)
Test case #17:	AC	[0,027s,	11,75 MB]	(1/1)
Test case #18:	AC	[0,029s,	11,88 MB]	(1/1)
Test case #19:	AC	[0,027s,	11,63 MB]	(1/1)
Test case #20:	AC	[0,026s,	11,63 MB]	(1/1)
Test case #21:	AC	[0,026s,	11,50 MB]	(1/1)
Test case #22:	AC	[0,028s,	11,75 MB]	(1/1)
Test case #23:	AC	[0,022s,	11,38 MB]	(1/1)
Test case #24:	AC	[0,029s,	11,75 MB]	(1/1)
Test case #25:	AC	[0,120s,	23,98 MB]	(1/1)
Test case #26:	AC	[0,151s,	24,97 MB]	(1/1)
Test case #27:	AC	[0,169s,	25,36 MB]	(1/1)
Test case #28:	AC	[0,173s,	25,69 MB]	(1/1)
Test case #29:	AC	[0,168s,	25,63 MB]	(1/1)
Test case #30:	AC	[0,167s,	25,61 MB]	(1/1)
Test case #31:	AC	[0,167s,	25,61 MB]	(1/1)
Test case #32:	WA	[0,171s,	25,72 MB]	(0/1)
Test case #33:	AC	[0,115s,	23,85 MB]	(1/1)
Test case #34:	AC	[0,022s,	11,38 MB]	(1/1)
Test case #35:	AC	[0,119s,	23,85 MB]	(1/1)
Test case #36:	AC	[0,119s,	23,71 MB]	(1/1)
Test case #37:	AC	[0,173s,	25,61 MB]	(1/1)
Test case #38:	AC	[0,137s,	24,35 MB]	(1/1)
Test case #39:	AC	[0,115s,	23,71 MB]	(1/1)
Test case #40:	AC	[0,111s,	21,34 MB]	(1/1)
Test case #41:	AC	[0,136s,	24,73 MB]	(1/1)
Test case #42:	AC	[0,176s,	25,41 MB]	(1/1)
Test case #43:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #44:	AC	[0,023s,	11,13 MB]	(1/1)
Test case #45:	AC	[0,022s,	11,38 MB]	(1/1)
Test case #46:	AC	[0,022s,	11,12 MB]	(1/1)
Test case #47:	AC	[0,022s,	11,38 MB]	(1/1)
'''





















