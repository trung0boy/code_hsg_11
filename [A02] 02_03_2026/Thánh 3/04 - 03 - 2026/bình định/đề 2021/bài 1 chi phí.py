import heapq
import sys
import random
import time

def randomA(n):
    A=[]
    for i in range(n):
        A.append(random.randint(1,100000))
    return A


n = int(sys.stdin.readline())
A= randomA(n)
#A = list(map(int,sys.stdin.readline().split()))

ans = 0
while len(A) > 1 :
    min1 = heapq.heappop(A)
    min2 = heapq.heappop(A)
    ans += ((min1 + min2)*0.05)
    heapq.heappush(A,min1+min2)
print(ans)
