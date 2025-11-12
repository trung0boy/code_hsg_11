
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


#=============================== 03 =================================
