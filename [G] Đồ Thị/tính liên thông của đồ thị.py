
import sys
'''
Kiểm tra tính liên thông và Đếm số thành phần liên thông
'''

sys.setrecursionlimit(10*6) # tăng giới hạn

def dfs(u,graph,visited): # kiểm tra tính liên thông và đếm đò thị
    visited[u] = True # gán đỉnh đã thăm
    for v in graph[u]: # lấy đỉnh liên kết với đỉnh u 
        if not visited[v]: # nếu đỉnh liên kết đó chưa thăm
            dfs(v,graph,visited) # tiếp tục dfs đỉnh tiếp đó 


def slove1(): 
    n , m = map(int,input().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    count=0
    visited = [False]*(n+1)
    for u in range(1,n+1): 
        if not visited[u]: # nếu false thì đò thị đó chưa thăm
            count+=1
            dfs(u,graph,visited) # gán all đỉnh liên kết = True
    print(count)
    
            
        
        





'''
Dạng 2: Tìm đường đi ngắn nhất (BFS)
'''
from collections import deque

def bfs_duong_di_ngan_nhat(n,graph,start,end):
    parent =[-1]*(n+1)
    q = deque()

    parent[start] = start
    q.append(start)

    while q:
        u = q.popleft()

        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                q.append(v)
    if parent[end] == -1:
        return 'NOT'
    else:
        print( 'YES')
            
    curr = end
    path =[]
    while curr != parent[curr]:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    print(path[::-1])

    
def slove2():
    n,m,s,e = map(int,sys.stdin.readline().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    print(bfs_duong_di_ngan_nhat(n,graph,s,e))




# bài mê cung

def mecung_bfs(matrix,n,m,start,end):

    q=deque()
    q.append(start)
    parent=[[-1]*m for i in range(n)] # gán đoạn đã đi chưa

    parent[start[0]][start[1]] =start # đánh dấu toạ độ start

    dx = [0,0,1,-1] # phải , trái , xuống, lên
    dy = [1,-1,0,0]
    while q:
        x,y =q.popleft()
        if (x,y) == end:
            return parent[x][y]
            break
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and parent[nx][ny] == -1 and matrix[nx][ny]==0:
                #parent[nx][ny]=parent[x][y]+1
                parent[nx][ny] =(x,y)
                q.append((nx,ny))
    if parent[end[0]][end[1]]==-1:
        print('n')  
    else:
        print('y')
       # print(parent[end[0]][end[1]]+1)
        print(parent)

    curr = tuple(end)
    path=[]

    while curr != parent[curr[0]][curr[1]]:
        path.append(curr)
        curr = parent[curr[0]][curr[1]]
    path.append(start)
    print(path[:len(path)-1])

    






"""
chu trình
"""
def has_cycle(u, p, graph, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            if has_cycle(v, u, graph, visited):
                return True
        elif v != p: # v đã thăm và không phải cha của u
            return True
    return False

# Trong hàm main:
# check = False
# for i in range(1, n + 1):
#     if not visited[i]:
#         if has_cycle(i, 0, graph, visited):
#             check = True; break






































         
