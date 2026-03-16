import sys
n,m = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

L = 0
R = max(A)
ans = 0
while L<R:
    mid = (L+R)//2
    cnt = 0
    if mid > 0:
        for x in A:
            cnt += (x//mid)
    if cnt > m:
        ans = mid
        L +=1
    else:
        R-=1
print(ans)










'''
1️⃣ Cắt gỗ

tìm chiều cao cưa lớn nhất

2️⃣ Cắt dây

tìm độ dài dây lớn nhất

3️⃣ Chia kẹo

tìm số kẹo mỗi phần lớn nhất

4️⃣ Sản xuất máy

tìm thời gian nhỏ nhất
'''
#====
        
'''

Test case #1:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #2:	AC	[0,022s,	10,99 MB]	(1/1)
Test case #3:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #4:	WA	[0,022s,	11,13 MB]	(0/1)
Test case #5:	WA	[0,022s,	11,00 MB]	(0/1)
Test case #6:	AC	[0,022s,	10,99 MB]	(1/1)
Test case #7:	AC	[0,021s,	11,13 MB]	(1/1)
Test case #8:	AC	[0,021s,	11,13 MB]	(1/1)
Test case #9:	WA	[0,021s,	11,13 MB]	(0/1)
Test case #10:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #11:	TLE	[>1,000s,	11,87 MB]	(0/1)
Test case #12:	TLE	[>1,000s,	11,75 MB]	(0/1)
Test case #13:	TLE	[>1,000s,	12,88 MB]	(0/1)
Test case #14:	TLE	[>1,000s,	12,13 MB]	(0/1)
Test case #15:	TLE	[>1,000s,	13,85 MB]	(0/1)
Test case #16:	TLE	[>1,000s,	13,63 MB]	(0/1)
Test case #17:	TLE	[>1,000s,	14,00 MB]	(0/1)
Test case #18:	TLE	[>1,000s,	11,75 MB]	(0/1)
Test case #19:	TLE	[>1,000s,	14,00 MB]	(0/1)
Test case #20:	TLE	[>1,000s,	12,75 MB]	(0/1)

'''
