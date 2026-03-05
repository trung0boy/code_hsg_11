import sys
import time
import random

def randomA(n):
    A=[]
    for i in range(n):
        A.append(random.randint(1,1000000000))
    return A

def randomQ(m):
    Q=[]
    for i in range(n):
        loai = random.randint(1,2)
        if loai == 1:
            u = random.randint(1,n)
            v =random.randint(1,1000000000)
            Q.append((loai,u,v))
        else:
            x = random.randint(1,n)
            y =random.randint(1,n)
            Q.append((loai,x,y))
    return Q


n,m = map(int,sys.stdin.readline().split())
#A = list(map(int,sys.stdin.readline().split()))
A = randomA(n)
Q = randomQ(m)
ans =0
s= time.time()
for loai,u,v in Q:
    #loai, u, v = map(int,sys.stdin.readline().split())
    if loai == 1:
        A[u-1] = v
    if loai == 2:
        ans+=1
        #print(sum(A[u-1:v]))
e = time.time()
print(e-s)
print('xong',ans)

'''
for i in range(m):
    loai, u, v = map(int,sys.stdin.readline().split())
    if loai == 1:
        A[u-1] = v
    if loai == 2:
        print(sum(A[u-1:v]))
'''

