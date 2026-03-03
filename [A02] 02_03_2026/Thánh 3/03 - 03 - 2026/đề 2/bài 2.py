import sys
import random
import time


def randomA(n):
    A=[]
    for i in range(n):
        A.append(random.randint(1,999999))
    return A


n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

#n = 1000000
#A = randomA(n)
'''
s = time.perf_counter()

n_A = max(A)

parent = [1]*(n_A+1)
for i in range(2,n_A+1):
    for j in range(i,n_A+1,i):
        parent[j] += i
ans = 0

for x in A:
    ans+=1
    
print('xong')
print(*[parent[x] for x in A])

e = time.perf_counter()
print(e-s)
'''

def prm(n):
    k = 2
    
    pos=[]
    while n != 1:
        count = 0
        while n%k ==0:
            count+=1
            n//=k
        if count > 0:
            pos.append((k,count))
        k+=1
    return pos

for x in A:
    a = prm(x)
    
    ans = 1
    for i in range(len(a)):
        ans *= int(((a[i][0]** (a[i][1]+1))-1) / (a[i][0]-1))
    print(ans)
        














