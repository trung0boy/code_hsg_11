import sys
import copy
# xoá cạnh 
def dfs_so_luong(u,graph,visited,count):
    visited[u] = 1
    for v in graph[u]:
        if visited[v] == 0:
            count = dfs_so_luong(v,graph,visited,count+1)
    return count
U = [0]
V = [0]
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    U.append(u)
    V.append(v)



res = 0
for i in range(1,n+1):
    graphB= copy.deepcopy(graph)
    graphB[U[i]].remove(V[i])
    graphB[V[i]].remove(U[i])
    
    visited = [0]*(n+1)
    
    cnt = 0
    ans = 1
    for u in range(1,n+1):
        if visited[u] == 0:
            cnt += 1
            ans *= dfs_so_luong(u,graphB,visited,1)
    if cnt > 1:
        res += ans
    else:
        res += 0

print(res)
























