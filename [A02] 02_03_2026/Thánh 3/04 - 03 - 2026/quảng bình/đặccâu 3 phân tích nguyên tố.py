import sys
def is_prime(n):
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            return False
    return True

def sang_eratosthene(n):
    m = [True]*(n+1)
    m[0]=m[1]=False
    for i in range(2,int(0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j]=False
    return [i for i in range(2,n+1) if m[i]]

def nguyen_to(n,prime):
    pos =[False]*(n+1)
    pos[0]=True
    parent =[-1]*(n+1)

    for p in prime:
        for s in range(n,p-1,-1):
            if pos[s-p] and not pos[s]:
                pos[s] = True
                parent[s] = p
    if not pos[n]:
        return False
    else:
        return True

    
n = int(sys.stdin.readline())
prime = sang_eratosthene(n)

for i in range(2,n+1):
    if is_prime(i):
        print(i)
    else:
        if nguyen_to(i,prime):
            print(i)
        















