import sys
l,r = map(int,sys.stdin.readline().split())

A = [1]*(r+1)
count = 0
for i in range(2,r+1):
    if A[i] + 1 == 3:
        count+=1
        print(i)
    for j in range(i,r+1,i):
        A[j] = A[j] + 1
print(count)
    
# luân kết thúc bằng 9 hoặc 1
