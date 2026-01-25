import time
import sys
input=sys.stdin.readline

def uoc(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count

def anti1(n):
    leght = 0
    for i in range(1,n+1):
        uoc1 = uoc(i)
        if uoc1 > leght:
            leght = uoc1
            print(i)
    return

# = = = = anti2 nhanh hơn cách anti1

# với 10^5 ≈ 0.41239356994628906
# với 10^6 ≈ 2.0889344215393066 với số này lại không hoạt động tốt
def anti2(n):
    start = time.time()

    m=[0]*(n+1) # mảng lưu số lượng ước của số đó nếu là bội
    for i in range(1,n+1):
        for j in range (i,n+1,i):
            m[j]+=1
            
    leght = 0
    for i in range(1,n):
        if m[i]>leght:
            leght = m[i]
            print(i)
    end = time.time()
    print(end - start)
        
n = int(input())

anti2(n)
