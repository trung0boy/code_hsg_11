import sys
import random
import numpy
import math
'''

def randomA(k):
    A=[]
    for i in range(n):
        u = random.randint(10,1000)
        v = random.randint(1,1000)
    return A




n,k,q0 = map(int,sys.stdin.readline().split())
parent =[0]*(n+1)
'''
n = 100000000
k = 1000
#Q = 

parent=[0]*(n+1)

for _ in range(k):
    l = random.randint(1,n)
    r = random.randint(l+1,n)
    #l,r = map(int,sys.stdin.readline().split())
    parent[l] += 1
    parent[r+1] -= 1
    
#Q = list(map(int,sys.stdin.readline().split()))
Q =[]
for i in range(1000):
    Q.append(random.randint(1,n))
#print(parent)

for i in range(1,n+1):
    parent[i] = parent[i-1]+ parent[i]
print("xong")
'''
for q in Q:
    print(parent[q])
'''
