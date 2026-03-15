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

#xử lí x # median
b = [x[i] - i for i in range(n)]
b.sort()
mid_b = b[n//2]
cnt_x = sum(abs(v - mid_b) for v in b)

#xử lí y # median
mid_y = y[n//2]
cnt_y = sum(abs(v - mid_y) for  v in y)

print(cnt_x + cnt_y)
# median
