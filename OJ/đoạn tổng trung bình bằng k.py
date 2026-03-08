import sys

n,k = map(int,sys.stdin.readline().split())
A= list(map(int,sys.stdin.readline().split()))
count = 0
curr = 0
pos ={}
for x in A:
    curr += (x-k)
    if curr in pos:
        count+=pos[curr]
    pos[curr] = pos.get(curr,0) + 1

print(count)




# A[l] + A[l+1] + ... + A[r]
#---------------------------- = k
#           r - l + 1
# <=> A[l] + A[l+1] + ... + A[r] == k(l-r+1)
#<=> A[l]-k + A[l+1]-k + ... + A[r]-k == 0
# khi đó mảng mới là các phần tử A[i] - k
# tìm tổng == 0 : A[l] == A[r]









