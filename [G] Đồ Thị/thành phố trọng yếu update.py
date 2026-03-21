import sys
import heapq
sys.stdin = open('3 thành phố trọng yếu.txt','r')
input = sys.stdin.readline

def dfs_lien_thong(u,graph,visited,count):
    visited[u] = True

    count+=1
    for v in graph[u]:
        if visited[v] == 0:
            count = dfs_lien_thong(v,graph,visited,count)
    return count


def thanh_pho_trong_yeu(n,graph):
    kq = [] # chứa độ quan trọng của thành phố i
    
    for i in range(1,n+1):
        visited =[0]*(n+1)
        visited[i] = -1
        
        count = 0
        ans = 1
        for u in range(1,n+1):
            if visited[u] == 0:
                count +=1
                ans *= dfs_lien_thong(u,graph,visited,0)
        if count > 1:
            kq.append(ans)
        else:
            kq.append(0)
    return kq




    
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

kq = thanh_pho_trong_yeu(n,graph)

x = sum(kq)/len(kq)
print(f'{x:.2f}')










