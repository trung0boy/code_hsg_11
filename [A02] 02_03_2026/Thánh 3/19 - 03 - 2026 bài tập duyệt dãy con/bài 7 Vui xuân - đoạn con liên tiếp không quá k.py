import sys
n,k = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

L = 0
curr = 0
ans = 0

for r in range(n):
    curr += A[r]
    while curr > k:
        curr -= A[L]
        L+=1
    ans = max(ans,r - L +1)
print(ans)
