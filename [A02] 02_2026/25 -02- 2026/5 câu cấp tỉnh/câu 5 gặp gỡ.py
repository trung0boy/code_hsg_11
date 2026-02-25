import sys
from collections import deque


def duong_di(n,graph,start,end):
    q = deque()
    q.append(start)

    parent =[-1]*(n+1)
    parent[start] = start

    while q:
        u = q.popleft()
        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                q.append(v)
    #print("y")

    curr = end
    path =[]
    while curr != parent[curr]:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    #print(path[::-1])
    return path[::-1]



def slove():
    n,q = map(int,sys.stdin.readline().split())
    graph =[[] for i in range(n+1)]
    Q =[]
    for _ in range(n-1):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    for _ in range(q):
        qi = list(map(int,sys.stdin.readline().split()))
        Q.append(qi)

        
    for u,s,e,a,b in Q:
        A = duong_di(n,graph,s,e) # danh sách là đường đi i tới j
        n_A = len(A)
        
        idx_u = A.index(u)
        
        if  idx_u > n_A - idx_u+1: # không tính u # trường hợp tới u
            ans_a = 0
            curr = float("inf")
            for i in range(n_A):
                if i <= idx_u :
                    ans_a += a*i
                else:
                    ans_a += b*i
            #print(ans_a)

            ans_b = 0
            for j in range(n_A-1,-1,-1):
        
                #print('j',j)
                
                if j > idx_u:
                    ans_b += a*(n_A-1-j)
                    curr = min(curr, (ans_a) + ans_b)
                    #print('curr',curr,ans_a,n_A-1-j)
                    ans_a  = (ans_a - b*j)
                elif j == idx_u:
                    ans_b +=a*(n_A-1-j)
                    curr = min(curr, (ans_a) + ans_b)
                    #print('curr',curr,ans_a, n_A-1-j)
                    ans_a = (ans_a - a*j)
                elif j < idx_u:
                    ans_b += b*(n_A-1-j)
                    curr = min(curr, (ans_a) + ans_b)
                    #print('curr',curr,ans_a,n_A-1-j)
                    ans_a = (ans_a - a*j)
            print(curr) # đây là kết quả


        if  idx_u <= n_A - idx_u+1: # trường hợp xa u
            ans_a = 0
            curr = float("inf")
            for i in range(n_A):
                if i <= idx_u :
                    ans_a += b*i
                else:
                    ans_a += a*i
            #print(ans_a)

            ans_b = 0
            for j in range(n_A-1,-1,-1):
        
                #print('j',j)
                
                if j > idx_u:
                    ans_b += b*(n_A-1-j)
                    curr = min(curr, (ans_a) + ans_b)
                    #print('curr',curr,"ans",ans_a,"j" ,n_A-1-j)
                    ans_a  = (ans_a - a*j)
                    
                elif j == idx_u:
                    ans_b +=b*(n_A-1-j)
                    curr = min(curr, (ans_a) + ans_b)
                    #print('curr',curr,"ans",ans_a,"j" ,n_A-1-j)
                    ans_a = (ans_a - b*j)
                    
                elif j < idx_u:
                    ans_b += a*(n_A-1-j)
                    curr = min(curr, (ans_a) + ans_b)
                    #print('curr',curr,"ans",ans_a,"j" ,n_A-1-j)
                    ans_a = (ans_a - b*j)
            print(curr) # đây là kết quả
                
        




#===== HAM RANDOM DO THI CAY=====

import random
import sys
sys.setrecursionlimit(10**7)

def generate_test():
    n = 10**3
    q = 100
    
    print(n, q)
    
    # ----- Sinh cây -----
    graph = [[] for _ in range(n + 1)]
    edges = []
    
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        graph[parent].append(i)
        graph[i].append(parent)
        edges.append((parent, i))
    
    for u, v in edges:
        print(u, v)
    
    # ----- LCA preprocessing -----
    LOG = 17  # vì 2^17 > 1e5
    parent = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    
    def dfs(u, p):
        parent[0][u] = p
        for v in graph[u]:
            if v != p:
                depth[v] = depth[u] + 1
                dfs(v, u)
    
    dfs(1, 0)
    
    for k in range(1, LOG):
        for i in range(1, n + 1):
            parent[k][i] = parent[k - 1][ parent[k - 1][i] ]
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        
        # đưa về cùng depth
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if diff & (1 << k):
                u = parent[k][u]
        
        if u == v:
            return u
        
        for k in reversed(range(LOG)):
            if parent[k][u] != parent[k][v]:
                u = parent[k][u]
                v = parent[k][v]
        
        return parent[0][u]
    
    def get_kth_ancestor(u, k):
        for i in range(LOG):
            if k & (1 << i):
                u = parent[i][u]
        return u
    
    # ----- Sinh truy vấn đảm bảo u nằm trên đường i->j -----
    for _ in range(q):
        i = random.randint(1, n)
        j = random.randint(1, n)
        
        L = lca(i, j)
        
        dist_i = depth[i] - depth[L]
        dist_j = depth[j] - depth[L]
        total_len = dist_i + dist_j
        
        # chọn 1 vị trí ngẫu nhiên trên đường đi
        pos = random.randint(0, total_len)
        
        if pos <= dist_i:
            u = get_kth_ancestor(i, pos)
        else:
            u = get_kth_ancestor(j, total_len - pos)
        
        a = random.randint(90000, 100000)
        b = random.randint(90000, 100000)
        
        print(u, i, j, a, b)


# generate_test()





        
        
