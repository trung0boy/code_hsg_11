import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
R = list(map(int,sys.stdin.readline().split()))

set_L = set(L)
set_R = set(R)

count = 0
for i in range(n):
    if L[i] not in set_R:
        count += 1
    if R[i] not in set_L:
        count +=1
print(count)


#4/5
