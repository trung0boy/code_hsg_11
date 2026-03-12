import sys
import copy
sys.stdin = open('x.dothikhopcau.inp','r')
input = sys.stdin.readline

def dfs_danh_dau(u,visited,graph):
    visited[u] = 1
    for v in graph[u]:
        if visited[v] == 0:
            dfs_danh_dau(v,visited,graph)


def so_lien_thong_goc(n,graph):
    visited =[0]*(n+1)
    count = 0
    for u in range(1,n+1):
        if visited[u] == 0:
            count+=1
            dfs_danh_dau(u,visited,graph)
    return count


def so_dinh_khop(n,LTG,graph):
    
    ans = 0
    for i in range(1,n+1):
        visited =[0]*(n+1)
        count = 0
        visited[i] = -1 # xoá đỉnh/khớp.
        for u in range(1,n+1):
            if visited[u] == 0:
                count+=1
                dfs_danh_dau(u,visited,graph)
        if count > LTG: # nếu làm tắng số thành phần liên thông.
            ans+=1
    return ans


def so_canh_cau(n,LTG,graphA,U,V):
    
    ans = 0
    #canh = []
    for i in range(1,n+1):
        graph = copy.deepcopy(graphA)
        graph[U[i]].remove(V[i])
        graph[V[i]].remove(U[i])
        
        visited =[0]*(n+1)
        count = 0
        for u in range(1,n+1):
            if visited[u] == 0:
                count+=1
                dfs_danh_dau(u,visited,graph)
        if count > LTG: # nếu làm tắng số thành phần liên thông.
            ans+=1
            #canh.append((U[i],V[i]))
        #print('cạnh',i,count,(U[i],V[i]))
    return ans



n,m = map(int,sys.stdin.readline().split())
graph =[[] for i in range(n+1)]
U = [0] # để xử lí xoá cạnh
V = [0] # để xử lí xoá cạnh
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    U.append(u)
    V.append(v)

LTG = so_lien_thong_goc(n,graph) # số thành phần liên thông ban đầu.
LTK = so_dinh_khop(n,LTG,graph) # số thành phần liên thông khi xoá đỉnh.
LTC = so_canh_cau(n,LTG,graph,U,V) # số thành phần liên thông khi xoá cạnh.

print(LTK, LTC)



















