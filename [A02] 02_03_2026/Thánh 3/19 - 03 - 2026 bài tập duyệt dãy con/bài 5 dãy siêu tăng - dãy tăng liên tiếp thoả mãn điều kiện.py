import sys




n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))


curr = A[0]
for i in range(1,n):
    if A[i] < curr:
        print(i+1)
        exit()
    curr += A[i]
print(0)
