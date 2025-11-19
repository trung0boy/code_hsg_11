#============================= thư viện ==============================

import math



#=============================== 01 =================================
"""
n so dau tien chia het cho 2 va ko chia het
"""
'''
def day_so_1(n):
    a=[]
    k=0 # đếm
    i=0 # chỉ số
    while k<n:
        if i%2==0 and i%3!=0:
            k+=1
            a.append(i)
        i+=1
    return a
n=10
print(day_so_1(n))
'''
#=============================== 02 =================================
"""
2 cho trước dãy A và B, len(B) < len(A). đếm số lần lặp ( có chồng lấn)
của dãy số B trong dãy số A
VD: B=[1,2,1], A={1,1,2,1,2,1,3,2,1,2,1] kết quả =3

"""
'''
def lan_lap(listA,listB):
    k=0 #dếm
    for i in range(len(listA) - len(listB) + 1):
        if listA[i:i+len(listB)] == listB:
            return i
    return -1
def Count(A,B):
    count = 0
    i=0
    while i< len(A)-len(B):
        k = lan_lap(A[i:],B)
        if k >= 0 :
            count+=1
        i+=1
        
    return count
A=[1,4,2,1,2,4,3,2,4,2,1]
B=[1,2,1]
print(Count(A,B))
'''

#=============================== 03 =================================
"""
tìm ước số nguyên tố của n kể cả n nếu n cũng là nguyên tố.
"""
'''
def nguyen_to(n):
    m=[True]*(n+1)
    m[0]=m[1]= False
    for i in range(2,int(math.sqrt(n))+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j]=False
    p=[i for i in range(n+1) if m[i]]
    return p

def primes(n):
    ket_qua=[]
    a=nguyen_to(n)
    for i in a:
        if n%i == 0:
            ket_qua.append(i)
    return ket_qua
print(primes(6))
'''        



#=============================== 04 =================================
"tìm trong hai sâu có dãy chung dài nhất"
'''
def day_chung(A,B):
    l_max=0 # độ dài lớn nhất tìm được.
    i_max=0 #chỉ số đầu tiên cuối cùng của dãy
    j_max=0 #chỉ số cuối cùng của dãy
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i:j] in B:
                if (j-i+1) > l_max:
                    l_max=(j-i)
                    i_max, j_max = i,j
    return l_max, i_max, j_max

a="aasdwrs"
b="jasdfro"
l,i,j=day_chung(a,b)
print(l,i,j) #độ dài max, chỉ số đầu, cuối.
print(l, a[i:j])
'''
#=============================== 05 =================================
""" kiểm xem số đó có phải nguyên tố ko"""


'''
while True:
#cách 1
    def nguyen_to(n): # nếu dùng kiểm 1 số sẽ bị chậm nếu n>1.10**7
        m=[True]*(n+1)
        m[0]=m[1]=False
        for i in range(2,int(math.sqrt(n))+1):
            if m[i]:
                for j in range(i*i,n+1,i):
                    m[j] = False
        return m[n]

#cách 2

    def nguyento2(n): # có thể đưa ra gần như lập tức
        if n<2:
            return False
        else:
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    return False
        return True


    n= int(input())
    print(nguyento2(n))

'''



#=============================== 06 =================================
""" sinh vô hạn số nguyên tố"""
'''
def primes(n):
    if n<2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                return False
    return True

i=1
k=0
while k<50:
    if primes(i)==True:
        print(i)
        k+=1
    i+=1
'''


#=============================== 07 =================================
test pull auto
















#=============================== 08 =================================





















#=============================== 09 =================================






