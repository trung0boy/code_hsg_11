import sys
sys.stdin = open('mạng máy tính.txt','r')
input = sys.stdin.readline

n,m = map(int,sys.stdin.readline().split())
graph =[[] for _ in range(n+1)]


for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)



num =[0]*(n+1)
low =[0]*(n+1)

stack =[]
time = 0
ans = 0

def tru_trinh_mang(u,p):
    global time,ans
    time +=1
    num[u] = low[u] = time
    
    for v in graph[u]:
        if v == p:
            continue
        if not num[v]:
            stack.append((u,v))
            tru_trinh_mang(v,u)
            low[u] = min(low[u],low[v])
            
            if low[v] >= num[u]:
                comb =set()
                while True:
                    a,b = stack.pop()
                    comb.add(a)
                    comb.add(b)
                    if (a,b) == (u,v) or (a,b) == (v,u):
                        break
                ans = max(ans,len(comb))
        elif num[v] < num[u]:
            stack.append((u,v))
            low[u] = min(low[u],num[v])
tru_trinh_mang(1,-1)
                
                
























