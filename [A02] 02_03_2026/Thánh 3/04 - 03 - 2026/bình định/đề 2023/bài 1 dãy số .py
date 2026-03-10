import sys
sys.stdin = open('bai1.INP','r')
input  = sys.stdin.readline

n,Q = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.append(float('inf'))
for _ in range(Q):
    ans = 0
    q = int(sys.stdin.readline())
    l = 0
    r = 0
    while r < n:
        while A[r] <= q:
           r+=1
        ans = max(ans,r-l)
        l = r+1
        r+=1
    print(ans)
    
        
        
            
    
        
