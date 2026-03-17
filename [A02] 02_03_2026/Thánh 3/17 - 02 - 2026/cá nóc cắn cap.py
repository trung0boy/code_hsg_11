import sys

n = int(sys.stdin.readline())
x =[]
y =[]

for _ in range(n):
    xi,yi =map(int,sys.stdin.readline().split())
    x.append(xi)
    y.append(yi)

x.sort()
y.sort()

b = [x[i] - i for i in range(n)]
b.sort()
mid_x = b[n//2]
cnt_x = sum(abs(v - mid_x) for v in b)

mid_y = y[n//2]
cnt_y = sum(abs(v - mid_y) for v in y)

print(cnt_x + cnt_y)
