import sys
sys.stdin = open('mạng máy tính.txt','r')
input = sys.stdin.readline



def tru_trinh_mang(u,p,graph,visited,count):
    visited[u] = True
    count+=1
    for v in graph[u]:
        if not visited[v]:
            TF, ans = tru_trinh_mang(v,u,graph,visited,count)
            if TF:
                #print('c1',ans)
                return True, ans
        elif v != p:
            count = 0
            #print('c2',count)
            
            return True, count
    #print('c3',count)
    
    return False,0







n,m = map(int,sys.stdin.readline().split())
graph =[[] for _ in range(n+1)]
visited =[False]*(n+1)


for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1,n+1):
    count = 0
    if not visited[i]:
        TF,ans = tru_trinh_mang(i,-1,graph,visited,count)
        if TF:
            print('i',ans)
            visited =[False]*(n+1)
        


















