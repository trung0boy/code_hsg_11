import sys
#sys.stdin = open('gift.txt','r')
#input = sys.stdin.readline


    
n ,k= map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

ans = 0

s = sum(A[:k])
for i in range(n-k+1):
    B = sorted(A[i:i+k])
    mid = B[k//2]
    ansK = 0
    for x in B:
        ansK += abs( x - mid)
    ans=max(ans,ansK)
print(ans)
    
