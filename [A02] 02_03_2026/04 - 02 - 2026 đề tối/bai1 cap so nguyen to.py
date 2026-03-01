import sys

def is_primes(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def miller_rabin(n): # tốt hơn is_prime 
    if n <2:
        return False
    small = [2,3,5,7,9,11]
    for p in small:
        if n == p:
            return True
        if n%p==0:
            return n==p
    d = n -1
    s=0
    while d%2==0:
        s+=1
        d//=2
    def check(a):
        x = pow(a,d,n)
        if x==1 or x == n-1:
            return True
        for _ in range(n-1):
            x = (x*x)%n
            if x==1:
                return True
        return False
    for a in (2,7,61):
        if a>=n:
            continue
        if not check(a):
            return False
    return True

    
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

count=0
for i in range(n):
    for j in range(i+1,n):
        if (A[i]+A[j])%2==0: # không xét chẵn
            continue
        if miller_rabin(A[i]+A[j]):
            count+=1
print(count)









