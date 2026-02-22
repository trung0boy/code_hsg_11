import sys
from collections import deque # hàm băm

def bfs_mang_may_tinh(n,A,start,end):
    q = deque() # băm
    q.append(start)

    parent = [-1]*(n+1) # -1 chưa thăm
    parent[start] = 0

    leght = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if parent[v] == -1: # nếu chưa thăm
                parent[v] = parent[u] + 1 # khi đi đến v sẽ là tổng bước trước +=1
                q.append(v) # thêm để đi tiếp
                
            
    if parent[end] == -1: # không có đường đi từ S->T
        return -1
    else: # nếu có đường đi thì parent[end] chích là kết quả
        return parent[end]
                
            
    


n, m = map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
S, T = map(int,sys.stdin.readline().split()) # tính cả T, không lấy S.

leght = bfs_mang_may_tinh(n,graph,S,T)
print(leght)














