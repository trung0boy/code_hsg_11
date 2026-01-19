import sys
input = sys.stdin.readline

def presic_sum(A,n):
    p=[0]*n
    p[0]=A[0]
    for i in range(1,n):
        p[i] = p[i-1]+A[i]
    return p

def sum_k(A,n,k):
    p=presic_sum(A,n)
    count=0
    for r in range(k,n):
        count = max(count,p[r]-p[r-k])
    print(count)
        
        

n,t,k = map(int,input().split()) # so phan tu, so day, doan k lon nhat
#a=[1,2,3,6,4,5,9,6,7,8]
#w=[1,2,3,12,6,5,8,2,3,2]

A=[0]*t
for i in range(t):
    A[i] = list(map(int,input().split()))
#print(A)

for i in A:
    sum_k(i,len(i),k)
