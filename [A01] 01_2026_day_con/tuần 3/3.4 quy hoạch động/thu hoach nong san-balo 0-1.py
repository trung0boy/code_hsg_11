n,W  = map(int,input().split())
w =[0]
v =[0]
for i in range(n):
    wi,vi = map(int,input().split())
    w.append(wi)
    v.append(vi)

A = [[0]*(W+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,W+1):
        A[i][j] = A[i-1][j]
        if j >= w[i]:
            A[i][j] = max (A[i-1][j], A[i-1][ j - w[i]] +v[i])
print(A[n][W])


M=W
i = n
posV=[]
while i != 0:
    if A[i][M] != A[i-1][M]:
        posV.append(v[i])
        M-=w[i]
    i-=1
print(posV)
        
