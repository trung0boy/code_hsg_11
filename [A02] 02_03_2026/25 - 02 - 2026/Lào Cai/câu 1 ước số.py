import sys
n = int(sys.stdin.readline())
A = []
for i in range(n):
    l,r = map(int,input().split())
    A.append(l*r)

n_max = max(A)
parent = [1]*(n_max+1) 

for i in range(1,n_max+1): # mảng chứa count ước đến max tích của A
    for j in range(2*i,n_max+1,i):
        parent[j] += 1

for i in A:
    print(parent[i]) # tại vị chí tích chính là kết quả
