from collections import deque
import sys


def bfs(graph,n):
    q =deque(*[graph[1]])
    parent = [-1]*(n+1)
    
    print('b',q)

    ans = 0
    while q:
        u = q.popleft()
        print('u',u)
        for v in graph[u]:
            print(q)
            if parent[v] == -1:
                parent[u] = u
                q.append(v)
                
                if u > v:
                    ans+=v
                else:
                    ans+=u
            print('ans',ans)
    print( ans)


n,m = map(int,sys.stdin.readline().split())
graph= [[]for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(graph,n))
     

