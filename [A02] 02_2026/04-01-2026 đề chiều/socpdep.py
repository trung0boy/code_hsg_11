

def tach(n):
    s = 0
    while n > 0:
        s = s*10 + n%10
        n//=10
    return s

def eratosthene(b):
    n=int(b**0.5)
    m=[True]*(n+1)
    for i in range(2,n+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j] = False
    return [i for i in range(2,n+1) if m[i]]
        

a,b=map(int,input().split())

count = 0
m = eratosthene(b)
for i in range(len(m)):
    if a <= m[i]**2 <= b and m[i] == tach(m[i]):
        count+=1
print(count)
