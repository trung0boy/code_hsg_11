import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

ans = float('inf')
l = 0
for r in range(10,n):
    while len(set(A[l:r+1])) == 12 :
        ans = min(ans,r-l+1)
        l+=1
if ans == float('inf'):
    print(0)
else:
    print(ans)
