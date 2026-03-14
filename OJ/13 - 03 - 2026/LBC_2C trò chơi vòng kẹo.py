import sys
#sys.stdin = open('LBC_2C trò chơi vòng kẹoT1.txt','r')
#input = sys.stdin.readline

n,Q = map(int,sys.stdin.readline().split())

parent = [0]*(n+1)
for q in range(Q):
    L,R = map(int,sys.stdin.readline().split())
    L-=1
    R-=1
    if L > R: # chỉ đi 1 chiều nên phải quay từ đầu.
        parent[0] += 1
        parent[L] += 1
        parent[R+1] -= 1
    else:
        parent[L] += 1
        parent[R+1] -= 1

mx = float('-inf')
curr = 0
for i in range(n):
    curr += parent[i]
    mx = max(mx,curr)
print(mx)

    
    
