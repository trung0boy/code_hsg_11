import sys
from collections import deque
sys.stdin = open('Bài 1. DENDUOC Đỉnh đến được.txt','r')

def bfs_count_dinh(n,graph,start):
    q = deque([start])
    parent = [-1]*(n+1)
    parent[start] = 1
    ans  = 1
    while q:
        u = q.popleft()
        for v in graph[u]:
            if parent[v] == -1:
                q.append(v)
                ans +=1
                parent[v] = u
    return ans

n,m,start = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
ans = bfs_count_dinh(n,graph,start)












































    
