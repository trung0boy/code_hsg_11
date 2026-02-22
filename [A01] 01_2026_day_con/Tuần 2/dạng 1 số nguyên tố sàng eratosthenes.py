def is_primes(n): # kiểm tra
    if n< 2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
    return True

def miller_rabin(n): # kiểm tra
    if n<2:
        return False
    small = (2,3,5,7,9,11)
    for p in small:
        if n == p:
            return True
        if n%p == 0:
            return n==p
    d = n-1
    s = 0
    while d%2 == 0:
        d//=2
        s+=1
    def check(a):
        x=pow(a,d,n)
        if x == 1 or x = n-1:
            return True
        for _ in range(s-1):
            x =(x*x)%n
            if x == n-1:
                return True
        return False
    for a in (2,7,61):
        if a>=n:
            continue
        if not check(a):
            return False
    return True




    
def sang_eratosthenes(n): # sàng
    m = [True]*(n+1)
    m[0]=m[1] =False
    for i in range(2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j] = False
    return [i for i in range(2,n+1) if m[i]]


    
