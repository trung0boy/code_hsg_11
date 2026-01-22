


def presic_sum(A):
    p=[0]*(len(A)+1)
    #p[0] = A[0]
    for i in range(1,len(A)+1):
       p[i] = p[i-1] + A[i-1]
    return p
    

n,q = map(int,input().split())
A=list(map(int,input().split()))
C=[]
p=presic_sum(A)
for i in range(q):
    l,r = map(int,input().split())
    C.append((p[r] - p[l-1]))
print(*C)
