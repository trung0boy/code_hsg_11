import sys

n,m,k = map(int,sys.stdin.readline().split())
A=[]
for _ in range(n):
    A.append(list(map(int,sys.stdin.readline().split())))

parent =[[0]*(m+1) for _ in range(n+1)]
         
for i in range(1,n+1):
    for j in range(1,m+1):
         parent[i][j] = (A[i-1][j-1] + parent[i][j-1]  +  parent[i-1][j]  -  parent[i-1][j-1])

max_sum = 0
for i in range(k,n+1):
    for j in range(k,m+1):
        max_sum = max(max_sum, parent[i][j] - parent[i-k][j] - parent[i][j-k] + parent[i-k][j-k])
print(max_sum)
            
                         
                         
                         
        
        
