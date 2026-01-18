from itertools import combinations

import sys
input = sys.stdin.readline

n=int(input())
A= list(map(int,input().split()))
count = 0
for x,y,z in combinations(A,3):
    if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        count+=1
print(count)
    
