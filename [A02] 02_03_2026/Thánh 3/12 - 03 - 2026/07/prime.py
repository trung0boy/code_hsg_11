import sys
import bisect
def eratosthene(n):
    m =[True]*(n+1)
    m[0]=m[1] = False
    for i in range(2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j] = False
    return [i for i in range(n+1) if m[i]]
    
m,n = map(int,sys.stdin.readline().split())

A =  []
for x in  eratosthene(m):
    if m%x == 0:
        A.append(x)
        
idx = bisect.bisect(A,n)

if idx == 0 and not A:
    print(-1)
elif idx == len(A):
    print(A[-1])
elif idx == 0 and A:
    print(A[0])
else:
    if abs(n - A[idx-1]) == abs(n - A[idx]):
        print(A[idx-1], A[idx])
    else:
        print(
                min(
                    abs(n - A[idx-1]),
                    abs(n - A[ idx])
                    )
            )
















        

