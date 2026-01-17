def bresic_sum(A,n):
    p=[0]*(n+1)
    p[0]=A[0]
    for i in range(n):
        p[i] = p[i-1] + A[i]
    return p

'''001
bài toán trạm phát sóng

Bài toán: Trạm phát sóng (WIFI)

Một con đường thẳng có N ngôi nhà,
ngôi nhà thứ i có số người là A[i].
Chính quyền muốn lắp đặt một trạm phát sóng có bán kính phủ
sóng là R. Nghĩa là nếu đặt trạm ở vị trí i,
nó sẽ phủ sóng được các nhà từ i−R đến i+R.
Hãy tìm vị trí đặt trạm sao cho tổng số người
được phục vụ là lớn nhất.

Phân tích:
Bán kính R⇒ Độ dài vùng phủ sóng là (i+R)−(i−R)+1=2R+1.
Đây chính là bài toán tìm đoạn con liên tiếp có độ dài K=2R+1
có tổng lớn nhất.
001'''

A=[1,2,1,2,2,1,2,3,4,2,2,1]
p=bresic_sum(A,len(A)) #mảng cộng dồn len(p)=len(A)
R = 2 #phạm vi bán kính
n = len(A)
k = 2*R+1
max_sum = -1
ir = -1

if n <= k: # trường hợp len(A) nhỏ hơn phạm vi
    print(sum(A))
    print(n//2+1) #vị trí đặt
else:
    
    for i in range(len(A)):
        #max_sum = max( max_sum, p[i] - p[i-k]) # nếu chỉ cần tổng max
        curr = p[i] - p[i-k]
        if curr > max_sum:
            max_sum = curr
            ir = i-R+1 # nếu cần vị trí đặt trạm
    print(max_sum,ir)


    
    
































