import sys

n,k = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))


ans = 0
for i in range(n):
    chan = 0
    le = 0
    for j in range(i,-1,-1):
        if A[j]%2 == 0:
            chan += A[j]
            #print(chan)
        if A[j]%2 != 0:
            le+=A[j]
        if 0 <= chan - le <= k and le !=0 and chan !=0:
            print(chan,le)
            ans+=1
print(ans)
