import sys
import time
import copy

def lien_thong(u,visited,graph): 
    visited[u] = u
    for v in graph[u]:
        if visited[v] == 0:
            lien_thong(v,visited,graph)




def check_khop():
    n,m = map(int,sys.stdin.readline().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        u,v =  map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)


    # -1 cạnh bị xoá.
    # 0 chưa thăm.
    # value đã thăm.
    count_goc = 0 #số thành phần liên thông ban đầu trước khi xoá khớp/đỉnh.
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i]==0:
            count_goc +=1
            lien_thong(i,visited,graph)

    ans = 0 # số lượng khớp thoả mãn # khi xoá đỉnh tạo ra nhiều liên thông.
    pos =[] # chứa khớp thoả mãn
    for u in range (1,n+1): # luần lượt xoá các khớp
        visited=[0]*(n+1)
        visited[u] = -1 # xoá
        count = 0
        for v in range(1,n+1):
            if visited[v]==0:
                count+=1
                lien_thong(v,visited,graph)
        if count > count_goc:
            ans+=1
            pos.append(u)
    print(count_goc,ans,pos)
            


        
        
def check_khop():
    n,m = map(int,sys.stdin.readline().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        u,v =  map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # -1 cạnh bị xoá.
    # 0 chưa thăm.
    # value đã thăm.
    count_goc = 0 #số thành phần liên thông ban đầu trước khi xoá khớp/đỉnh.
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i]==0:
            count_goc +=1
            lien_thong(i,visited,graph)

    ans = 0
    for u in range(m):
        graph_b = graph
        if v[i] in b_copy[u[i]]:
        b[u[i]].remove(v[i])
        if u[i] in b_copy[v[i]]:
        b[v[i]].remove(u[i])

        count=0
        visited=[0]*(n+1)
        for v in range(1,n+1):
            if visited[v]==0:
                count+=1
                lien_thong(v,visited,graph)
        if count > count_goc:
            ans +=1
    print(ans)
























    
