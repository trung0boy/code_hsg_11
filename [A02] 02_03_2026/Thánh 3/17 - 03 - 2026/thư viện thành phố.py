import sys
sys.setrecursionlimit(10**6)

def dfs_lien_thong(u,graph,visited,cost,ans):
    visited[u] = True
    ans = min(ans,cost[u])
    for v in graph[u]:
        if not visited[v]:
            ans = dfs_lien_thong(v,graph,visited,cost,ans)
    return ans

n,m = map(int,sys.stdin.readline().split())
cost= [0] + list(map(int,sys.stdin.readline().split()))
graph = [[] for i in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
visited = [False]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        ans+= dfs_lien_thong(i,graph,visited,cost,float('inf'))
print(ans)
    
