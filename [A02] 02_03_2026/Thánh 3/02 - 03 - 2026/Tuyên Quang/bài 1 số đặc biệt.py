import sys

n= int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))
ans = 0
for x in A:
    if x%10 == 8 or x%10 == 6:
        ans+=x
print(ans)
