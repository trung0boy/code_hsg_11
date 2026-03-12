import sys
import heapq
sys.stdin = open('1 nối Thành phố.txt','r')
input = sys.stdin.readline

def dfs_lien_thong(u,graph,visited,count):
    visited[u] = True

    count+=1
    for v in graph[u]:
        if not visited[v]:
            count = dfs_lien_thong(v,graph,visited,count)
    return count



n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


visited =[False]*(n+1)
parent = [0] # lưu số liên thông của mỗi đỉnh

for i in range(1,n+1):
    if not visited[i]:
        count = dfs_lien_thong(i,graph,visited,0)
        parent.append(count)

parent.sort()
print(parent[-1] + parent[-2])




























