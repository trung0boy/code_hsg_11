import sys
n,M = map(int,sys.stdin.readline().split())
w=[0]
v=[0]

for _ in range(n):
    wi, vi = map(int,sys.stdin.readline().split()) #trọng lượng, giá trị.
    w.append(wi)
    v.append(vi)

A = [[0]*(M+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,M+1):
        A[i][j]=A[i-1][j]
        if j >= w[i]:
            A[i][j] = max(A[i-1][j], A[i-1][j - w[i]] + v[i])
        


















"""
inp
5 15
12 4
2 2
1 1
1 2
4 10
"""
