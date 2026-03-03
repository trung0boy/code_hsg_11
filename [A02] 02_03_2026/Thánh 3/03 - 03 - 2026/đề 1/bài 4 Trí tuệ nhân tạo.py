import sys

n,q = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

# đếm khi đoạn thoả mãn: u <= l <= r <= v
'''
count = 0
for _ in range(q):
    U,V = map(int,sys.stdin.readline().split())
    U -= 1
    V -= 1
    L = U-1
    R = V-1
    while L <R:
        if A[U] <= A[L] and A[L] <= A[R] and A[R] <= A[V]:
            count+=1
            print("một")
            R-=1
        elif A[U] <= A[L] and A[L] <= A[R] and A[R]  >   A[V]:
            R-=1
            print("hai")
        elif A[U]  >  A[L] and A[L] <= A[R] and A[R] <= A[V]:
            L+=1
            print("ba")
        else:
            R -=1
print(count)
'''

for _ in range(q):
    count = 0
    u,v = map(int,sys.stdin.readline().split())
    U = u -1
    V =v -1
    
    for L in range(U,v):
        R = v-1
        while L < R and (A[R] > A[V]) :
            R-=1
            
        if A[U] <= A[L] and A[L] <= A[R] and A[R] <= A[V] and A[L] != A[R]:
            count+=1
            print(A[L:R+1])
            R-=1
    print(count)
            
        
        






















    
