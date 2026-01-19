def eratosthenes(n):
    p=[True]*(n+1)
    p[0]=p[1]=False
    for i in range(2,n):
        if p[i]:
            for j in range(i*i,n,i):
                p[j]=False
    return [i for i in range(2,n) if p[i]]
a =eratosthenes(10**4) # 10**4
print(a)
