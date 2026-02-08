def tru_trinh(u,p,graph,visited,ans):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            if tru_trinh(u,p,graph,visited,ans+1):
                return ans
        elif p!=v:
            return ans
    return False








import sys
n,m = map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    u,v =n,m = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited =[False]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        if tru_trinh(i,0,graph,visited,0):
            print()
