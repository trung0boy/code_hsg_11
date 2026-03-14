import sys
from collections import deque
#sys.stdin = open('EVA sơ tán.txt','r')
#input = sys.stdin.readline


def bfs_duong_di(Exit,graph,n):
    kq = [float('inf')]*(n+1)
    q = deque()
    while Exit:
        parent = [-1]*(n+1) # lưu
        check = [False]*(n+1) # check

        start = Exit.pop()
        q.append(start)
        check[start] =True
        
        parent[start] = 0
        kq[start] = 0
        while q:
            u = q.popleft() # phải tính từ kề đỉnh u nên sẽ lấy cái cũ nhất
            for v in graph[u]:
                if not check[v] and v not in Exit: # đỉnh chưa đến và không trong exit
                    parent[v] = parent[u] + 1
                    q.append(v)
                    kq[v] = min(kq[v], parent[u]+1)
                    check[v] = True
    return kq

a = list(map(int, sys.stdin.readline().split()))
if len(a)==2:
    n,k=a
else:
    n=a[0]
    k = int(sys.stdin.readline())

#n,k =map(int, sys.stdin.readline().split()) # số phòng, số nhà thoát.
#n = int(sys.stdin.readline())
#k = int(sys.stdin.readline())

Exit = list(map(int, sys.stdin.readline().split())) # chứa phòng thoát hiểm.
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


kq = bfs_duong_di(Exit,graph,n)

print(*kq[1:])












