from collections import Counter

import sys
input = sys.stdin.readline



def bresic_sum(a,n): # bresic_sum tổng dồn
    q=[0]*(n+1)
    for i in range(1,n+1):
        q[i] = q[i-1] + a[i-1]
    return q

#   =   =   =



A1  =[1,23,43,32,35,0,6,7,2,34,78,5] # sử dụng test cho bài toán 1
q=bresic_sum(A1,len(A1))
print(q[5] - q[2-1]) # in ra sum từ l - r


'''
Bài toán 1: Tìm số lượng đoạn con (L,R) có tổng đúng bằng K.
Kỹ thuật: Ta có Sum(L,R)=P[R]−P[L−1]=K⇒P[L−1]=P[R]−K.
Khi duyệt đến R, ta tìm xem trong các P trước đó đã có
bao nhiêu giá trị bằng (P[R]−K).

'''
q1 = bresic_sum(A1,len(A1))
k=67
kq=0
#print(q1)

for r in range(1,len(A1)+1):

    if q1[r] - k in q1:
        kq+=1
        print('q',q1[r])
print(kq) #kết quả



'''
Bài toán 2: Tìm đoạn con dài nhất có tổng bằng 0.
'''

A2= [12,-5,0,27,-14,8,3,-9,21,-1,6,-18,15,4,-7,19,-3,10,-11,2,25,-36,7,-2,13] #sử dụng cho bài toán 2

q2 = bresic_sum(A2,len(A2))
print(q2)
cq2 = Counter(q1)































