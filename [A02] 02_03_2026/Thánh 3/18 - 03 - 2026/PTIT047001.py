import sys
n = int(sys.stdin.readline())
A= list(map(int,sys.stdin.readline().split()))



def uoc(n):
    temp = n
    i = 1
    ans  = 0
    while i*i <= temp:
        if temp % i == 0:
            ans += i
           
            if i*i != n:
                ans += temp//i

        temp//i
        i+=1

    return ans
            
        

ans = 0
p_max = 0
a = 0
ai = 0
aj = 0
p=0
for j in range(n):
    u = 0
    v = 0
    for i in range(j):
        if A[i] > A[j]:
            u += 1
            #if ai == -1:
                #ai = A[i]
    for k in range(j+1,n):
        if A[k] < A[j]:
            v += 1
    if u > 0 and v > 0:
        p = u*v
        ai = uoc(A[j])
    if p > p_max:
        
        p_max = p
        aj = A[j]
if p_max == 0:
    print('Neu khong co Thuong, Tai se buon biet may :(.')
else:
    print(uoc(aj),aj)

        

'''
Test case #1:	AC	[0,022s,	10,88 MB]	(1/1)
Test case #2:	AC	[0,022s,	10,88 MB]	(1/1)
Test case #3:	AC	[0,023s,	11,13 MB]	(1/1)
Test case #4:	WA	[0,023s,	11,00 MB]	(0/1)----
Test case #5:	WA	[0,022s,	11,13 MB]	(0/1)----
Test case #6:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #7:	TLE	[>1,000s,	12,13 MB]	(0/1)----
Test case #8:	TLE	[>1,000s,	12,00 MB]	(0/1)----
Test case #9:	TLE	[>1,000s,	12,00 MB]	(0/1)----
Test case #10:	TLE	[>1,000s,	11,88 MB]	(0/1)----
Test case #11:	TLE	[>1,000s,	12,00 MB]	(0/1)----
Test case #12:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #13:	AC	[0,022s,	10,88 MB]	(1/1)
Test case #14:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #15:	AC	[0,022s,	10,87 MB]	(1/1)
Test case #16:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #17:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #18:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #19:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #20:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #21:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #22:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #23:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #24:	AC	[0,023s,	11,12 MB]	(1/1)
Test case #25:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #26:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #27:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #28:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #29:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #30:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #31:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #32:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #33:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #34:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #35:	WA	[0,022s,	11,25 MB]	(0/1)----
Test case #36:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #37:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #38:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #39:	AC	[0,023s,	11,13 MB]	(1/1)
Test case #40:	AC	[0,022s,	11,25 MB]	(1/1)

'''
