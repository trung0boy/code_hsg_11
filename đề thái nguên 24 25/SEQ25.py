import sys

def day_hon_k(n,A,k):
    
    leght_max = 0
    leght = 0
    for r in range(n+1):
        if A[r] >= k:
            leght += 1
        else:
            if leght > leght_max:
                leght_max = leght
                leght = 0
    return leght_max
        
n , Qi = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.append(-float('inf'))
Q = []
for i in range(Qi):
    k= int(sys.stdin.readline())
    Q.append(k)

Am =max(A)
for k in Q:
    if k > Am:
        print(0)
    else:
        print(day_hon_k(n,A,k) )

