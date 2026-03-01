import sys
import time
import random

def randomA(n):
    A=[]
    for i in range(n):
        A.append(random.randint(1000,1000000))
    return A


A = randomA(1000)





#n = int(sys.stdin.readline())
#A= list(map(int,sys.stdin.readline().split()))
start = time.time()
count = 0
for x in A:
    s =x//10
    if x%10 > s%10 :
        
        count+=x
end = time.time()
print(end - start)
print(count)



