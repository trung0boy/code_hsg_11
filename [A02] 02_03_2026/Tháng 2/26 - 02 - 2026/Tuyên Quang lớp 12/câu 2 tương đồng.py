import sys


import time
import random

def randomA(n):
    A=[]
    for i in range(n):
        A.append(random.randint(10,1000000))
    return A
A = randomA(100000) +[float("inf")]
k = 29
n =100000
#n,k = map(int,sys.stdin.readline().split())
#A = list(map(int,sys.stdin.readline().split())) + [float('inf')]
#A.sort()

i = 0
start = time.time()
count = 0
for i in range(n-1):
    j = i + 1
    while A[j] - A[i] <= k:
        count+=1
        j+=1
end = time.time()
print(end - start)
print(count)

