
def to_hop(k):
    for i in range(A[k-1]+1, n-K+k+1):
        A[k]=i
        if k == K:
            print(A[1:])
        else:
            to_hop(k+1)
        





n,  K = map(int,input().split())
              
A=[0]*(K+1)
to_hop(0)
