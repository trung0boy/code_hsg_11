import sys
n,k = map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))


ans = 0
curr = 0
pos ={0:1}
for x in A:
    curr +=x
    if curr - k in pos:
        ans+=pos[curr-k]
    pos[curr] =pos.get(curr,0)+1
print(ans)


#= = = = = = == = = = =
ans = 0
curr = 0
l=0
for i in range(n):
    curr += A[i]
    while curr>k:
        curr -=A[l]
        l+=1
    if curr == k:
        ans+=1

print(ans)
