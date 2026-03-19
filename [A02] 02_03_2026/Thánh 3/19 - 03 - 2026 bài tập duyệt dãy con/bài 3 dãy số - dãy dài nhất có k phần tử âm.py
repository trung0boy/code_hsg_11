import sys

n,k = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

ans = 0
cnt = 0 # đếm số lượng số âm của trong đoạn con hiện tại.
curr = 0
l = 0
for r in range(n):
    curr += A[r]
    if A[r] < 0:
        cnt += 1
    while cnt > k and l < n:
        if A[l] < 0:
            cnt -= 1
        curr -= A[l]
        l += 1
    ans = max(ans,curr)
    print(A[l:r+1])
print(ans)
