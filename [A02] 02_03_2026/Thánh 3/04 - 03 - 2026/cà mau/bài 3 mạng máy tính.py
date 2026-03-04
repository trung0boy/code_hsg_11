import sys
import random
import time

def randomA(n,m):
    A = [[] for i in range(n+1)]
    for i in range(m):
        u = random.randint(1,n+1)
        v = random.randint(1,n+1)
        A[u].append(v)
        A[v].append(u)
    return A




def dfs_danh_dau(u,graph,visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs_danh_dau(v,graph,visited)




n = 1000000
m = 100000
#n,m = map(int,sys.stdin.readline().split())

'''
graph =[[] for i in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
'''
graph = randomA(n,m)

count = 0
visited =[False]*(n+1)

for i in range(1,n+1):
    if not visited[i]:
        count += 1
        dfs_danh_dau(i,graph,visited)
print(count)


#8#












































