import sys

n = int(sys.stdin.readline())
x1 = 1
x2 = 1
for i in range(n):
    x1,x2 = x2, x1+x2
print(x2)
    
