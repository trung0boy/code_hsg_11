import sys

n = int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

ans = float('-inf')
min_curr = float('inf')
curr = 0
for x in A:
    curr += x
    if min_curr > curr:
        min_curr = curr
    ans = max(ans , curr - min_curr)
print(ans)

'''
Test case #1:	Kết quả đúng (AC)	[0,029s,	10,40 MB]	(0/0)
Test case #2:	Kết quả đúng (AC)	[0,030s,	10,41 MB]	(4/4)
Test case #3:	Kết quả đúng (AC)	[0,031s,	10,39 MB]	(4/4)
Test case #4:	Kết quả đúng (AC)	[0,032s,	10,39 MB]	(4/4)
Test case #5:	Kết quả đúng (AC)	[0,030s,	10,38 MB]	(4/4)
Test case #6:	Kết quả sai (WA)	[0,031s,	10,49 MB]	(0/4)
Test case #7:	Kết quả đúng (AC)	[0,032s,	10,86 MB]	(4/4)
Test case #8:	Kết quả đúng (AC)	[0,033s,	10,87 MB]	(4/4)
Test case #9:	Kết quả đúng (AC)	[0,031s,	10,95 MB]	(4/4)
Test case #10:	Kết quả đúng (AC)	[0,035s,	10,94 MB]	(4/4)
Test case #11:	Kết quả sai (WA)	[0,033s,	10,98 MB]	(0/4)
Test case #12:	Kết quả đúng (AC)	[0,065s,	19,88 MB]	(4/4)
Test case #13:	Kết quả đúng (AC)	[0,062s,	19,89 MB]	(4/4)
Test case #14:	Kết quả đúng (AC)	[0,070s,	19,88 MB]	(4/4)
Test case #15:	Kết quả đúng (AC)	[0,066s,	19,84 MB]	(4/4)
Test case #16:	Kết quả đúng (AC)	[0,069s,	19,88 MB]	(4/4)
Test case #17:	Kết quả đúng (AC)	[0,068s,	19,88 MB]	(4/4)
Test case #18:	Kết quả đúng (AC)	[0,072s,	20,73 MB]	(4/4)
Test case #19:	Kết quả đúng (AC)	[0,070s,	20,75 MB]	(4/4)
Test case #20:	Kết quả đúng (AC)	[0,078s,	20,76 MB]	(4/4)
Test case #21:	Kết quả đúng (AC)	[0,073s,	20,77 MB]	(4/4)
Test case #22:	Kết quả đúng (AC)	[0,073s,	20,77 MB]	(4/4)
Test case #23:	Kết quả đúng (AC)	[0,079s,	20,76 MB]	(4/4)
Test case #24:	Kết quả đúng (AC)	[0,074s,	20,80 MB]	(4/4)
Test case #25:	Kết quả đúng (AC)	[0,086s,	20,79 MB]	(4/4)
Test case #26:	Kết quả sai (WA)	[0,078s,	20,90 MB]	(0/4)
'''









