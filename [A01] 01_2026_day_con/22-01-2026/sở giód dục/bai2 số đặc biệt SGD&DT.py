#
import time

def eratosthenes(R): #sàng và lấy bình phương
    n=int(R**0.5) # chỉ cần đến bình phương của R
    m = [True]*(n+1)
    m[0] = m[1] = False
    for i in range(2,n+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j]=False
    return [i*i for i in range(n+1) if m[i]]

def so_dac_biet1(L,R):
    start = time.time()
    count=0
    A_primes_bp =eratosthenes(R)
    #print(A_primes_bp)
    for i in A_primes_bp: # chỉ cần duyệt bình phương nguyên tố 
        if L <= i <= R: # nếu tồn tại trong khoảng L - R là thoả mãn
            #print(i)
            count+=1
    end = time.time()
    print('time',end - start)
    return count


# = = =    C1 nhanh hơn C2

def primes(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return n*n

def so_dac_biet2(L,R):
    count=0

    for i in range(L,R):
        if primes(i) and L <= primes(i) <=R: 
            count+=1
    return count
















