import sys
sys.setrecursionlimit(10**9)
def eratosthene(n):
    m = [True]*(n+1)
    m[0]=m[1]=False
    for i in range(2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j] = False
    return set([i for i in range(2,n+1) if m[i]])



n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

a = max(A)
nguyen_to = eratosthene(a)

cnt = 0
for x in A:
    if x not in nguyen_to:
        cnt += 1
        
Cn = (n*(n-1))//2
Ck = (cnt*(cnt-1))//2
print(Cn - Ck )





































