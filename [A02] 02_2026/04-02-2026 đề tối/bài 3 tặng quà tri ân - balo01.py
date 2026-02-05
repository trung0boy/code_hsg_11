import sys

n , W = map(int,sys.stdin.readline().split())

w,v=[0],[0]
for i in range (n):
    wi , vi = map(int,sys.stdin.readline().split())
    w.append(wi)
    v.append(vi)
A=[[0]*(W+1) for i in range(n+1) ]

for i in range(1,n+1):
    for j in range(1,W+1):
        A[i][j] = A[i-1][j]
        if j>=w[i]:
            A[i][j] = max(A[i-1][j],A[i-1][j-w[i]]+v[i])
print(A[n][W])
    
