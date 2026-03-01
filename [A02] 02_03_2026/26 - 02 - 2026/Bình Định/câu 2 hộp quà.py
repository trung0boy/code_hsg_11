

def chia_keo(A,B,n,m):
    j = 0
    count = 0
    if max(A) < max(B): # nếu giá trị kẹo lớn nhất nhỏ hơn giá trị kẹo cần đạt dừng luân
            return -1
    for i in range(n):
        if j < len(B): # để khi hết B[i] thì sau không cần nữa
            if A[i] >= B[j] :
                count+=A[i]
                j+=1
        else:
            return count
            break

        




import sys

n,m = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

A.sort()
B.sort()


print(chia_keo(A,B,n,m))
