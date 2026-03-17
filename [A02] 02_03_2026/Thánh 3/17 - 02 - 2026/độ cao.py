import sys


def tach(n,h):
    ans = 0
    while n>0:
        ans += n%10
        n//=10
    return ans == h

def eratosthene(n,h):
    primes = [True]*(n+1)
    primes[0] = primes[1] = False
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i,n+1,i):
                 primes[j] = False
    leght = 0
    for i in range(2,n+1):
        if primes[i] and tach(i,h):
            leght+=1
            print(i)
    print(leght)



n = int(sys.stdin.readline())
h = int(sys.stdin.readline())

eratosthene(n,h)

























