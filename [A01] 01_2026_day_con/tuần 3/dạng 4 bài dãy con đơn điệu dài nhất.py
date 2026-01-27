n = int(input())
A = list(map(int,input().split()))
pos =[1]*(n)

for i in range(n):
    for j in range(i):
        if A[i] > A[j] and pos[j]+1 > pos[i]:
            pos[i] = pos[j]+1
print(pos)

max_leght=max(pos) # độ dài lớn nhất

idx = pos.index(max_leght) # chỉ số của số lớn nhất


"""
# trường hợp chỉ có 1 dãy liên tiếp và chỉ lấy 1 dãy
pos_value = [A[idx]] # pos lưu value
i =idx

while i>0:
    if pos[i] != pos[i-1]:
        pos_value.append(A[i-1])
    i-=1
print(pos_value)
"""
# trường hợp có niều hơn 1 dãy. nếu độ dài lớn nhất chứa trong pos có nhiều hơn 1
# ta thêm một vòng lặp nữa để lấy hết số lớn nhất đó
# sau khi đã lấy ta gán độ dài lớn nhất tại vị trí đó trong danh sách thành -1 đã dùng

while idx in pos: # nếu độ dài lớn nhất đó vẫn tòn tại trong pox ta vẫn xét
    i =pos.index(max(pos))
    pos_value = [A[idx]] # pos lưu value # lưu luân giá trị cuối. sau đó chỉ cần thêm A[i-1]
    Ai = pos[i]
    while i>0:
        if pos[i] != pos[i-1] and pos[i-1] != -1:
            pos_value.append(A[i-1])
            Ai = pos[i-1]
        i-=1
    print(pos_value)
    pos[pos.index(max(pos))] = -1
    
# có 4 trường hợp có thể xảy ra
#pos[i] != pos[i-1] and pos[i-1] != -1: chỉ xét được TH 1,2,3 không xét được 4
# chỉ só 1 max_leght
    # dãy đó số lớn nhất ở cuối
    # dãy đó số lớn nhất ở giữa
# có nhiều hơn 1 max_leght
    # dãy đó số lớn nhất liên tiếp pos               =   [1, 2, 2, 3, 4, 4]
    # dãy đó số lớn nhất ở giữa và ở cuối pos  = [1, 2, 3, 4, 1, 2, 3, 4] 






