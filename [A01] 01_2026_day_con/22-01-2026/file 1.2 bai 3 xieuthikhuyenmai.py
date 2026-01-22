
#BÀI 3: SIÊU THỊ KHUYẾN MÃI
#Mô tả: Siêu thị có N mặt hàng đang niêm yết với giá P1,P2,…,PN. Để tri ân khách hàng,
#siêu thị tung ra M chương trình giảm giá.
#Mỗi chương trình giảm giá thứ i sẽ giảm Di đồng cho các mặt hàng có số thứ tự từ Li đến Ri.
#Hãy xác định giá cuối cùng của từng mặt hàng sau khi áp dụng tất cả các chương trình giảm giá.
#(Nếu giá giảm lớn hơn giá gốc, giá mặt hàng đó bằng 0).

n,m = map(int,input().split())
p=list(map(int,input().split()))

A=[0]*(n+2) #mảng hiệu
for i in range(m):
    L,R,K = map(int,input().split())
    L-=1
    R-=1
    A[L]+=K
    A[R+1]-=K

curr=0
for i in range(n):
    curr+=A[i] # tổng dồn của mảng hiệu
    p[i]-=curr
    if p[i]<0:
        p[i]=0
print(p)

















