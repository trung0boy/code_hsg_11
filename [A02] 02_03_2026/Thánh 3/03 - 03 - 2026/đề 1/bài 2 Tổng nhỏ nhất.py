import sys
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

min1 = float('inf')
min2 = float('inf')

for x in A:
    if x < min1:
        min2 = min1
        min1 = x
    elif x < min2:
        min2 = x
print(min1, min2)
