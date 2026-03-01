import sys
import random
import time
def randomA(n):
    A=[]
    for i in range(n):
        A.append(random.randint(1,1000000))
    return A
from collections import deque




'''
n =5000
A = randomA(n)
'''

"""
start = time.time()
count = 0
for l in range(n-1):
    max_home = 0
    for r in range(l+1,n):
        if max_home < A[l] and max_home < A[r]:
            count+=1
            max_home = max(max_home,A[r])
end = time.time()
print(end - start)
print(count)
"""

n =int( sys.stdin.readline())
A = list(map(int,input().split()))


pos = []
count =0

for x in A:
    ans=1
    while pos and x > pos[-1][0]:
        count+=pos[-1][1]
        pos.pop()
        
    #if not pos:
     #   pos.append([x,1])
        
    if pos and x == pos[-1][0] :
        ans = pos[-1][1]
        count+=ans
        pos.pop()
        
        if pos:
            count+=1
        pos.append([x,ans+1])
    else :
        if pos:
            count+=1
        pos.append([x,1])

print(count)
            
        
        
        
        
    
















