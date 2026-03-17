import sys


def dfs_so_luong(u,graph,visited,count):
    visited[u] = 1
    for v in graph[u]:
        if visited[v] == 0:
            count = dfs_so_luong(v,graph,visited,count+1)
    return count

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)
cntG = 0
for u in range(1,n+1):
    if visited[u] == 0:
        cntG+= 1
        x = dfs_so_luong(u,graph,visited,1)

res = 0
for i in range(1,n+1):
    visited = [0]*(n+1)
    visited[i] = -1

    cnt = 0
    ans = 1
    for u in range(1,n+1):
        if visited[u] == 0:
            cnt += 1
            ans *= dfs_so_luong(u,graph,visited,1)
    if cnt > cntG:
        res += ans
    else:
        res += 0
x = res/n
print(f'{x:.2f}')


























