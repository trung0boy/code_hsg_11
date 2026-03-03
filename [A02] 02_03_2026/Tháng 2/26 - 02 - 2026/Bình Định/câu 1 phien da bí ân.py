import sys

n,k = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

pos ={0:1}

curr = 0
count = 0

for x in A:
    curr += x
    if curr - k in pos:
        count += pos[curr-k]
    pos[curr] = pos.get(curr,0)+1
print(count)
        
