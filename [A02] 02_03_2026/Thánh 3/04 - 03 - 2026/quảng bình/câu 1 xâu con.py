import sys

n,m = map(int,sys.stdin.readline().split())
A = str(input())
B = str(input())


i = 0
j = 0

while j < len(B)-1 and i < len(A)-1:
    if A[i] == B[j]:
        i +=1
    j+=1
if i == len(A)-1:
    print('Y')
else:
    print('N')
