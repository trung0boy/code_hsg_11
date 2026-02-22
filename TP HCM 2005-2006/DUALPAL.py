import sys

def primes(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def so_doi(n,s):
    for i in range(s,200):
        
        
        











n,s = map(int,sys.stdin.readline().split())


