"""
import sys

# Tăng giới hạn đệ quy để tránh lỗi với đồ thị sâu
sys.setrecursionlimit(100)

def solve():
    # Đọc dữ liệu
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    # Đọc m cạnh, lưu ý có thể có đa đồ thị (nhiều chuyến bay giữa 2 sân bay)
    # Tuy nhiên, đa cạnh thì không bao giờ là cầu.
    for i in range(2, 2 + 2 * m, 2):
        u = int(input_data[i])
        v = int(input_data[i+1])
        if u == v: continue
        adj[u].append(v)
        adj[v].append(u)

    low = [0] * (n + 1) # cũ nhất có thể quay lại
    num = [0] * (n + 1) # hiện thời
    size = [0] * (n + 1) 
    timer = 0
    total_cohesion = 0

    def dfs(u, p):
        nonlocal timer, total_cohesion
        timer += 1
        num[u] = low[u] = timer
        size[u] = 1
        
        for v in adj[u]:
            if v == p:
                continue
            if num[v]:
                low[u] = min(low[u], num[v])
            else:
                dfs(v, u)
                size[u] += size[v]
                low[u] = min(low[u], low[v])
                
                # Điều kiện kiểm tra cạnh (u, v) có phải là cầu không
                if low[v] > num[u]:
                    # Cạnh này là cầu, nó đóng góp vào k * (n - k) cặp
                    count_pairs = size[v] * (n - size[v])
                    total_cohesion += count_pairs

    # Vì đồ thị luôn liên thông nên chỉ cần DFS từ đỉnh 1
    if n > 0:
        dfs(1, -1)
    
    print(total_cohesion)

if __name__ == "__main__":
    solve()





"""









































































import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
m = int(input())
graph =[[] for _ in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    graph[u].append((v,i))
    graph[v].append((u,i))

num = [0]*(n+1) # thứ tự vào.
low = [0]*(n+1) # cũ nhất có thể về.
timer = 0 # lần lượt đỉnh.

ans = 0

def dfs(u,p):
    global timer, ans
    timer += 1
    low[u] = num[u] = timer
    size = 1
    for v,e in graph[u]:
        if e == p:
            continue
        
        if not num[v]:
            child_size = dfs(v,e)
            size += child_size
                
            low[u] = min(low[u], low[v])
            if low[v] > num[u]:
                ans += child_size*(n - child_size)
        else:
            low[u] = min(low[u],num[v])
                
    return size
dfs(1,-1)
print(ans)







