
import sys
from collections import deque
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
dạng 3 chu trình
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

def slove3():
    n,m= map(int,sys.stdin.readline().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    visited=[False]*(n+1)
    for i in range(1,n+1):
        if not visited[i]:
            if has_cycle(u, p, graph, visited):
                print('y')
                break
            else:
                print('n')

def thanh_kiem(u,p,graph,visited):
    visited[u]=True
    for v in graph[u]:
        if not visited[v]:
            if thanh_kiem(v,u,graph,visited):
                return True
        elif p!=v:
            return True
    return False



def slove4():
    n,m = map(int,sys.stdin.readline().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    visited=[False]*(n+1)
    for i in range(1,n+1):
        if not visited[i]:
            if thanh_kiem:
                print('y')
                break
            else:
                print('n')
    


'''
dạng4 kiểm tra đồ thị 2 phía
'''
'''
Thử tô màu đồ thị bằng 2 màu (0 và 1).
Nếu đỉnh hiện tại màu 0, các đỉnh kề nó phải màu 1.
Nếu trong quá trình tô gặp một đỉnh đã có màu mà màu đó trùng với
đỉnh hiện tại → Không phải đồ thị hai phía.
'''

def hai_phia(n,graph):
    color = [-1]*(n+1) # ban đầu chưa thăm -1
    for i in range(1,n+1):
        if color[i]==-1:
            q = deque([i])
            color[i]=0
            while q:
                u = deque.popleft(q)
                for v in graph[u]:
                    if color[v]==-1:
                        color[v] =1-color[u]
                        q.append(v)
                    elif color[v]==color[u]:
                        return False
    return True
    


def slove5():
    n,m = map(int,sys.stdin.readline().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    if hai_phia(n,graph):
        print('không trùng lặp')
    else:
        print('có trùng lập')




def ket_ban(n,graph): # đồ thị 2 phía
    color =[-1]*(n+1)
    for i in range(1,n+1):
        if color[i] ==-1:
            q = deque([i])
            color[i]=0
            while q:
                u =deque.popleft(q)
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[u] == color[v]:
                        return False
    return True


def slove6():
    n,m = map(int,sys.stdin.readline().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    if ket_ban(n,graph):
        print('không trùng lặp')
    else:
        print('có trùng lập')


#= = = = = = = = = = =


def duong_di(u,p,f,graph,W,curr):
    if u==f: # khi u đã đến đích f ta cộng nốt tại u
        return curr + W[u-1]
    Max_sum = -float('inf') # có thể bỏ được trường hợp số âm
    for v in graph[u]: # bắt đầu thăm từ đỉnh kề của u
        if v!=p: # tránh cộng ngược
            res = duong_di(v,u,f,graph,W,curr + W[u-1]) # u -1 vì n đi từ 1 đến n+1/ quy hoạch động
            Max_sum = max(Max_sum, res)
    return Max_sum

def slovebt1():
    n,m = map(int,input().split())
    s,f =map(int,input().split()) # đi từ s đến f
    W=list(map(int,input().split()))
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    ans = duong_di(s,0,f,graph,W,0)
    print(ans)




'''
Bài 2: Đỉnh "Vàng" trong mạng lưới (Mức độ: Trung bình)
Đề bài: Cho đồ thị không trọng số. Mỗi đỉnh được gán một giá trị Wi.
Tìm khoảng cách ngắn nhất từ đỉnh S đến một đỉnh Vàng (đỉnh có Wi≥K).
•	Thuật toán: Đây là bài toán BFS (Breadth-First Search).
•	Điểm mấu chốt: Vì cạnh không có trọng số,
ta dùng BFS để tìm đường đi ngắn nhất (số cạnh ít nhất).
Khi vừa chạm vào một đỉnh thỏa mãn Wi≥K, đó chính là đáp án.
'''
def bfs_dinh_vang(start,k,n,graph,W):
    q=deque([start])
    parent=[-1]*(n+1) # lưu độ dài và đã thăm
    parent[start]=0 # bắt đàu =0
    while q:
        u = deque.popleft(q)
        if W[u] >=k: # nếu thoả mã 
            return parent[u],u # tại parent u chính là độ dài
        for v in graph[u]:
            if parent[v]==-1:
                parent[v] = parent[u]+1 # từ đỉnh u đến đỉnh tiếp thì độ dài sẽ+1 cho đến khi thoả mãn k
                q.append(v)
    return -1,-1

def slovebt2():
    n,m = map(int,input().split())
    s,k =map(int,input().split()) # đi từ s đến f
    W=list(map(int,input().split()))
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    ans = bfs_dinh_vang(s,k,n,graph,W)
    print(ans)










         
