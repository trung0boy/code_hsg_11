import sys
def lien_thong(u,graph,visited,c):
    visited[u] = 1
    c+=1
    
    for v in graph[u]:
        if visited[v] == 0:
            lien_thong(v,graph,visited,c)
            return c
        

n,m = map(int,sys.stdin.readline().split())
graph= [[]for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)        
countG = 0
for i in range(n+1):
    if  visited[i] == 0:
        countG+=1
        lien_thong(u,graph,visited,0)
# 0: chưa thăm, -1:bị xoá.
dp = [0]*(n+1)
for i in range(n+1):
    visited = [0]*(n+1) 
    visited[i] = -1 # xoá đỉnh.

    count = 0
    d = []
    c = 0
    for j in range(n+1):
        if  visited[j] == 0:
            count+=1
            c = lien_thong(j,graph,visited,0)
        d.append(c)
        c = 0
    if count == 1:
        continue
    else:
        for k in range(len(d)):
            dp[i] = dp[i]*d[k]
    print('d',d)
            
print(round(sum(dp)/len(dp),2))
        

























        
    
