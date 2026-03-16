import sys

n = int(input())
x = []
y = []

for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

#xử lí x 
b = [x[i] - i for i in range(n)]
b.sort()
mid_b = b[n//2]
cnt_x = sum(abs(v - mid_b) for v in b)

#xử lí y 
mid_y = y[n//2]
cnt_y = sum(abs(v - mid_y) for  v in y)

print(cnt_x + cnt_y)














'''
Test case #1:	AC	[0,023s,	11,25 MB]	(1/1)
Test case #2:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #3:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #4:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #5:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #6:	AC	[0,023s,	11,25 MB]	(1/1)
Test case #7:	AC	[0,023s,	11,13 MB]	(1/1)
Test case #8:	AC	[0,023s,	11,25 MB]	(1/1)
Test case #9:	AC	[0,074s,	29,81 MB]	(1/1)
Test case #10:	AC	[0,308s,	116,52 MB]	(1/1)

'''















































#median
