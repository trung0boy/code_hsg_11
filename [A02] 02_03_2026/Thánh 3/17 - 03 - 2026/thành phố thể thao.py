import sys

def dfs_TP(u,graph,visited,cnt):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            cnt = dfs_TP(v,graph,visited,cnt+1)
    return cnt



n,m = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)
parent = []
for i in range (1,n+1):
    if not visited[i]:
        cnt = dfs_TP(i,graph,visited,1)
        parent.append(cnt)
parent.sort()
print(parent[-1] + parent[-2])
        
