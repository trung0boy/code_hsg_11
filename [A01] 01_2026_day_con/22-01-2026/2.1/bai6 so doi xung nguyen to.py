import time

def dao(n):
    c = 0
    while n>0:
        c = c*10 + n%10
        n//=10
    return c

def eratosthenes(L,R): #R = 10**6 ≈ 0.1389787197113037 hoạt động cực kì tốt
                       #R = 10^7 ≈ 1.4436395168304443
    start = time.time()
    n=R
    m=[True]*(n+1)
    m[0]=m[1]=False
    for i in range(2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j]=False
    end =time.time()
    print(end - start)
    print(*[i for i in range(L,R+1) if m[i] and i == dao(i)])
    return
