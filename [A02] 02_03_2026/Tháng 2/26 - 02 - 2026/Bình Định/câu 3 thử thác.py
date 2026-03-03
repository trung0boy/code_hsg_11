import sys


def thu_thach(k,a,b):
    if k == 1:
        return -1
    i = 1
    
    while k > 0:
        if i % a == 0 or i%b == 0:
            i+=1
        else:
            k-=1
            i+=1
    return i-1
        





    
T = int(sys.stdin.readline())
Q =[]
for _ in range(T):
    k0,a0,b0 = map(int,sys.stdin.readline().split())
    Q.append((k0,a0,b0))

for k,a,b in Q:
    print(thu_thach(k,a,b))



