from collections import Counter

import sys
input = sys.stdin.readline



def bresic_sum(a,n): # bresic_sum tổng dồn
    q=[0]*(n)
    q[0]=a[0]
    for i in range(1,n):
        q[i] = q[i-1] + a[i]
    return q

#   =   =   =


"""001
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
điều kiện để bresic sum có tổng đoạn = 0 khi q[r] = q[l-1]

duyệt A lưu lại vị trí của R đã từng xuất hiện trước đó.
lưu vào pos{<giá trị q[r]>:<chỉ số của q[r]>}
nếu gặp lại thì tìm lại vị trí của số đó

'''

A2= [12,-5,0,27,-14,8,3,-9,21,-1,6,-18,15,4,-7,19,-3,10,-11,2,25,-36,7,-2,13] #sử dụng cho bài toán 2 và bài toán 3


q2 = bresic_sum(A2,len(A2))


ans=0
n=len(A2)
pos ={0:-1} # {<giá trị> : <chỉ số tại vị trí của giá trị>}
for r in range(1,len(A2)):
    if q2[r] in pos: # q2[L] đã xuất hiện thì lấy chỉ số
        ans = max(ans,r - pos[q2[r]])
    else:
        pos[q2[r]] = r
print(ans)

    

'''
Bài toán 3 (Số dư): Tìm đoạn con có tổng chia hết cho K.
Kỹ thuật: Sử dụng tính chất (P[R]−P[L−1])(modK)=0⇒P[R](modK)=P[L−1](modK).
lưu số dư nếu đã
tạo pos3={0:1} ban đầu đã có để kt
sau khi chia %  nếu thấy thì đếm +=1 và giá trị đư +=1
else thêm dư đó vào

'''
k=3

pos3={0:1}
ans3=0
curr_sum = 0

for i in A2:
    curr_sum += i
    du = curr_sum%k
    if du in pos3:
        ans3 += 1
        pos3[du]+=1
        #print('s',curr_sum)
    else:
        pos3[du]=1

print(ans3)
#print(pos3)        

001"""

'''
Dạng 3: Mảng hiệu (Difference Array) - "Ngược" với mảng cộng dồn
Đây là dạng bài cực hay, dùng để xử lý các truy vấn cập nhật đoạn.
Bài toán: Cho mảng A ban đầu toàn số 0. Có Q thao tác: "Cộng thêm giá trị V
vào tất cả phần tử từ vị trí L đến R". Sau Q thao tác, hãy in ra mảng cuối cùng.
Kỹ thuật:
    Tạo mảng hiệu D có N+2 phần tử.
    Với mỗi thao tác (L,R,V):
    D[L] += V
    D[R + 1] -= V
    Mảng kết quả A[i] chính là mảng cộng dồn của mảng D: A[i] = A[i-1] + D[i].
Dấu hiệu nhận biết: Đề bài yêu cầu thay đổi giá trị trên một vùng/đoạn
nhiều lần và chỉ hỏi kết quả cuối cùng.

'''


'''005
Dạng 4: Kết hợp với Kỹ thuật "Cửa sổ trượt" (Sliding Window)
•	Bài toán: Cho dãy số A và số K. Tìm đoạn con liên tiếp có độ dài đúng
    bằng K sao cho tổng của chúng là lớn nhất.
•	Cách giải: * Tính mảng cộng dồn P.
o	Duyệt i từ K đến N: Tìm Max(P[i]−P[i−K]).
•	Ứng dụng: Bài toán "Trồng cây", "Đặt trạm thu phát sóng"
    (tìm vị trí đặt trạm để phủ được nhiều nhà nhất trong phạm vi K).
005'''

A4=[2,5,2,2,3,1,3]
k=3
p4 = bresic_sum(A4,len(A4)) # 
ans_max = 0
ai=aj=0

ansp=0
print('A4',A4)
print('p4',p4)
for r in range(k,len(A4)):
    ans_max = max(ans_max,  p4[r]-p4[r-k])
    print(p4[r]-p4[r-k])
print(ans_max)
#print(len(A4))
#print(len(p4))



'''
B1: Số đoạn con có tổng bằng K (Prefix Sum + Dictionary)
Bài toán: Cho dãy số A và số nguyên K.
Đếm số lượng đoạn con liên tiếp có tổng đúng bằng K.
•	Dữ liệu: N≤105,K có thể âm hoặc dương.
•	Thuật toán: Khi duyệt đến vị trí i có tổng cộng dồn là S, ta cần tìm xem trước đó có bao nhiêu vị trí j mà tổng cộng dồn là S−K. Vì S−(S−K)=K. Ta dùng một Dictionary để lưu tần suất xuất hiện của các tổng trước đó.
'''
A5= [12,-5,0,27,-14,8,3,-9,21,-1,6,-18,15,4,-7,19,-3,10,-11,2,25,-36,7,-2,13]







