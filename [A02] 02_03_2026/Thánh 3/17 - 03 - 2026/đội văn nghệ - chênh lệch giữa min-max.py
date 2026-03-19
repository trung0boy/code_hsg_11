import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

A.sort()
k = 5
ans = float('inf')
for r in range(k-1,n):
    ans = min(ans, A[r] - A[r-k+1])
    #print(A[r] , A[r-k+1])
print(ans)
    
#            150 155 161 172 170 152 169
