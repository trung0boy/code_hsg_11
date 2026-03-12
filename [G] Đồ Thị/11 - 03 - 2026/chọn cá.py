import sys
A = list(map(int,sys.stdin.readline().split()))

A.sort

ban1 = 0
ban2 = 0
for i in range(len(A)-1, -1,-1):
    if ban1 >= ban2:
        ban2 += A[i]
    else:
        ban1 += A[i]
print(abs(ban1-ban2))
    
