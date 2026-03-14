import sys

def prefix(A):
    p = [0]*(n+1)
    p[0]=A[0]
    for i in range(1,n+1):
        p[i] = p[i-1] + A[i]
    return p

n,k = map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))

p = prefix(A)

for r in range(k,n+1):
    ans = max(ans(p    
