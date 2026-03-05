import sys

n = int(sys.stdin.readline())
A= list(map(int,sys.stdin.readline().split()))

ans = 0



for i in range(len(A)-2):
    parent = [0,float('inf'),float('inf')] # lớn nhất, min 1, min 2
    for j in range(i+1,len(A)):
        parent[0] = A[i]
        if parent[1] > A[j]:
            parent[2] = parent[1]
            parent[1] = A[j]
            ans = max( ans, (parent[0]*2) - parent[1] - parent[2] )
        if parent[1] < A[j] and parent[2] > A[j]:
            parent[2] = A[j]
            
        ans = max(ans, (parent[0]*2) - parent[1] - parent[2] )
print(ans)
