
'''
Bài 3: Đoạn con có số lượng số chẵn bằng số lượng số lẻ
Đề bài: Cho dãy A gồm N số nguyên dương. Tìm số lượng đoạn con liên tiếp có số lượng số chẵn bằng số lượng số lẻ.
Dữ liệu: N≤106.
Thuật toán (Kỹ thuật quy đổi):
Đây là bài toán ẩn dụ. Ta quy đổi: Nếu A[i] chẵn, gán B[i]=1. Nếu A[i] lẻ, gán B[i]=−1.
Một đoạn con có số chẵn bằng số lẻ khi và chỉ khi tổng các phần tử tương ứng trong mảng B bằng 0.
Bài toán trở về: Tìm số đoạn con của B có tổng bằng K=0.
'''
A=[1,2,1,2,2,1,2,3,4,2,2,1]
n=len(A)



#p=[0]*(n)
curr=0
pos = {0:1}
ans=0
for i in range(n):

    if A[i]%2==0: # nếu chẵn =1
        curr += 1
    else: # nếu lẻ =-1
        curr -= 1
    if curr in pos: #khi tổng bằng 0 nghĩa là đoạn đó TM và tồn tại trong pos
        ans += pos[curr] 
        pos[curr] = +1
    else:
        pos[curr] = 1
    print(pos)
print(ans)

