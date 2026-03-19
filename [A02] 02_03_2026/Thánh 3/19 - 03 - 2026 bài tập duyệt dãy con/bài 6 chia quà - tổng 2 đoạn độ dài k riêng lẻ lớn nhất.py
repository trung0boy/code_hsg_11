import sys

n,k = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

prefix = [0] * (n+1)
for i in range(n): # tổng dồn.
    prefix[i+1] = prefix[i] + A[i]
print('prefix',prefix)

m = n-k+1
mid_prefix=[0]*(m+1)
for i in range(1,m+1): # tổng từng đoạn k phần tử.
    mid_prefix[i] = prefix[i+k-1] - prefix[i-1]
print('mid_prefix',mid_prefix)

ans = 0
for i in range(1,m-k):
    for j in range(i+k,m):
        ans = max(ans,mid_prefix[i] + mid_prefix[j])
        print(mid_prefix[i] , mid_prefix[j])
print(ans)
        
