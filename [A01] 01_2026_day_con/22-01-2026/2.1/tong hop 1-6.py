import math

import sys
input = sys.stdin.readline



# = = = = = = = = =#

#BÀI 1: CẶP SỐ THÂN THIẾT (Tổng ước số)< chưa được>

#BÀI 2: TRUY VẤN SỐ NGUYÊN TỐ

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
s=s = s = max(R for L, R in A)
p=prefic(s) #lấy R lớn nhất
print(s)
for L,R in A:
    print(p[R]-p[L-1])
    
# = = = = = = = = =#

#BÀI 3: PHÂN TÍCH THỪA SỐ NGUYÊN TỐ
#nếu dùng cho n <= 3.10^6 thì hoạt động tốt
def eratosthene(n): # sàng gốc
    m=[True]*(n+1)
    m[0]=m[1]=False
    for i in range(2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j] = False
    return [i for i in range(n) if m[i]]

# = = =
def spf_primes(n): #gán bội của nguyên tố thành nguyên tố nhỏ nhất
    fps=[0]*(n+1)
    for i in range(2,n+1):
        if fps[i] == 0:
            fps[i]=i
            for j in range(i*i,n+1,i):
                if fps[j]==0:
                    fps[j] = i
    return fps

def factorzize(n):  # phân tích thừa số
    pos = {}
    spf = spf_primes(n)
    while n > 1:
        p = spf[n]
        pos[p] = pos.get(p,0)+1
        n//=p
    print('*'.join(f'{k}^{v}'for k,v in pos.items()))
    return

N = int(input())
factorzize(N)

# = = = = = = = = =#

#BÀI 4: ƯỚC CHUNG LỚN NHẤT CỦA GIAI THỪA

# factorial một hàm mạnh để tính giai thừa của thư viện math
n,m = map(int,input().split())
print(math.gcd(math.factorial(n),math.factorial(n)))

# = = = = = = = = =#

#BÀI 5: SỐ PHẢN NGUYÊN TỐ (Antiprime Number)

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

#anti2 nhanh hơn cách anti1

# với 10^5 ≈ 0.41239356994628906
# với 10^6 ≈ 2.0889344215393066 với số này lại không hoạt động tốt
def anti2(n):
    m=[0]*(n+1) # mảng lưu số lượng ước của số đó nếu là bội
    for i in range(1,n+1):
        for j in range (i,n+1,i):
            m[j]+=1
            
    leght = 0
    for i in range(1,n):
        if m[i]>leght:
            leght = m[i]
            print(i)
        
n = int(input())
anti2(n)

# = = = = = = = = =#

#BÀI 6: SỐ ĐỐI XỨNG NGUYÊN TỐ (Palindromic Prime)

def dao(n):
    c = 0
    while n>0:
        c = c*10 + n%10
        n//=10
    return c

def eratosthenes(L,R): #R = 10**6 ≈ 0.1389787197113037 hoạt động cực kì tốt
                       #R = 10^7 ≈ 1.4436395168304443
    n=R
    m=[True]*(n+1)
    m[0]=m[1]=False
    for i in range(2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j]=False
    end =time.time()
    print(*[i for i in range(L,R+1) if m[i] and i == dao(i)])
    return

# = = = = = = = = =#
