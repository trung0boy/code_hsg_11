import sys
from collections import deque
def bfs_duong_di(graph,start,end):
    q = deque()
    parent = [-1]*(n+1)

    q.append(start)
    parent[start] = start
    print(parent)

    while q:
        u = q.popleft()

        
        for v in graph[u]:
            if v == end:
                return parent[u] + v
            if parent[v] == -1:
                parent[v] = parent[u] + v
                q.append(v)
    #print(parent[end])


n,q = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
Q=[]
for _ in range(n-1):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for _ in range(q):
    si, ei = map(int,sys.stdin.readline().split())
    #Q.append((si,ei))
    if si == ei:
        print(si)
    else:
        print(bfs_duong_di(graph,si,ei))

    
    
    


