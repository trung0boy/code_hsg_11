import sys
from collections import deque


def tuyen_duong_hieu_qua(n,graph,start,end):
    q = deque()
    parent =[-1]*(n+1)

    q.append(start)
    parent[start] = start
    
    while q:
        u = q.popleft()
        for v in graph[u]: 
            if parent[v[0]] == -1:
                q.append(v)
                 
    
            
    

n,m = map(int,sys.stdin.readline().split())

graph =[[] for i in range(n+1)]
for _ in range(m):
    u,v, map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
tuyen_duong_hieu_qua(n,graph,1,n)

