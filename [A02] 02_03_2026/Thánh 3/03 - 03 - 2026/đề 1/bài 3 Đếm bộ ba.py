import sys

n = int(sys.stdin.readline())

A= list(map(int,sys.stdin.readline().split()))

A.sort()
count = 0
for k in range(n):
    i = 0
    j = k-1
    while i<j:
        s = A[i] + A[j]
        if s == A[k]:
            count+=1
            i+=1
            j-=1
        elif s < A[k]:
            i+=1
        else:
            j-=1
print(count)

'''
tổng ba số i,j,k khác nhau.
đặt k là tổng lớn nhất cần tìm
trở thành tìm 2 số nhỏ hơn k để tổn thoả mã điều kiện.
'''
