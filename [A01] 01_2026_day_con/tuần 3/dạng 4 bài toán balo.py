
#def backpack():
n, W = map(int, input().split())
    
w =[0]
v =[0]
for i in range(1, n + 1):
    vi,wi = map(int, input().split())
    w.append(wi)
    v.append(vi)
    
A= [[0]*(W+1) for _ in range(n+1)]
#print(A)
for i in range(1,n+1): # chỉ số
    for j in range(1,W+1): # khối lượng j
        A[i][j] = A[i-1][j] # cọt j hàng i
        if j >= w[i]: # nếu khối lương đang xét lớn hơn 
            A[i][j] = max(A[i-1][j], A[i-1][j-w[i]]+v[i]) # số nào lớn hơn thì lấy # khối lượng hiện tại j
                                                                                # trừ bới khối lượng lấy # tương ứng còn lại
                                                                                # thì xét tiếp
                                                                                # dồng thời phải cộng thêm giá trị của khối lượng
                                                                                # lấy đó
print(A)

i = n
m = W
pos =[]

while i!=0:
    if A[i][m] != A[i-1][m]:
        pos.append(v[i])
        m-=w[i]
    i-=1
print(pos[::-1])
