import sys
input = sys.stdin.readline
def eratosthenes(n):
    m=[True]*(n+1)
    m[0]=m[1]=False
    for i in range (2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j] = False
    return m

def prefic(n_max): # mảng chứa tổng số lượng nguyên tố
    m=eratosthenes(n_max)
    p=[0]*(n_max+1)
    for i in range(1,n_max+1):
        p[i] = p[i-1]+ (1 if m[i] else 0) # nếu vị trí nào là số nguyên tố thì +=1 tiếp tục
    return p
    

A=[]
Q=int(input())
for i in range(Q):
    L,R = map(int,input().split())
    A.append((L,R))
s = max(R for L, R in A)
p=prefic(s) #lấy R lớn nhất
print(s)
for L,R in A:
    print(p[R]-p[L-1])

