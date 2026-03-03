import time


def tach(n):
    s = 0
    while n > 0:
        s = s*10 + n%10
        n//=10
    return s
        

def is_prime(n):
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n = int(input())
s = tach(n)
if is_prime(n) and is_prime(s):
    print(1)
else:
    print(0)

