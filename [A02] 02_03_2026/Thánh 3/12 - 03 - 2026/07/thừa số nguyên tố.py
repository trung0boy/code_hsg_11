import sys


def phan_tich_primes(n):
    k=2
    ans = 0
    while n != 1:
        while n%k == 0:
            ans +=1
            n//=k
        k+=1
    return ans

def tichA(i):
    tich = 1
    for x in A[:i]:
        tich*=x
    for x in A[i+1:]:
        tich*=x
    kq = phan_tich_primes(tich)
    return kq


n = int(sys.stdin.readline())
A= list(map(int,sys.stdin.readline().split()))

tich = 1
ans = float('inf')

for i in range(n):
    ans = min(ans,tichA(i))
    
print(ans)














