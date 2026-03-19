import sys
sys.setrecursionlimit(10**6)
n,k = map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))

prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + A[i]





m = n-k+1
pos = [0]*(m+1)
for i in range(1,m+1):
    pos[i] = prefix[i+k-1] - prefix[i-1]
print(pos)

# max từ trái qua phỉa
L = [0]*(m+1)
L[0]=pos[0]
for i in range(1,m):
    L[i] = max(L[i-1],pos[i])

#max từ phải qua trái
R =[0]*(m+2)
R[m-1]=pos[m-1]
for i in range(m,-1,-1):
    R[i] = max(R[i+1], pos[i])


res = float('inf')
for i in range(1,m):
    ans = 0
    if i-k >= 1:
        ans = max(ans, L[i-k])
    if i+k <= m:
        ans = max(ans, R[i+k])
    res = min(res,ans)
print(res)



















    
