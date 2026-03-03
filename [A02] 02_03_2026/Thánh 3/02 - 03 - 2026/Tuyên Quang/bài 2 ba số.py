import sys

n,k = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

count = 0
for x in A:
    if x%k == 0:
        count+=1
ans = (count * (count - 1))//2

print(ans)
