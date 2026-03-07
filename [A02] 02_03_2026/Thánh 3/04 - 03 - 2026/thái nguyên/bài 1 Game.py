import sys

sys.stdin = open('bai1.INP',  'r')
input = sys.stdin.readline

n = int(sys.stdin.readline())
A=[[0]*(n+1)]
for i in range(10):
    a = [0] + list(sys.stdin.readline().strip())
    A.append(a)
i =10
j =1

def quay_lui(i,j,up_side_count,start,xet,list_count,visited): 
    if j == n:
        return True, list_count
    visited[i][j] = True
    #print(i,j,list_count)
    if i == 1 or i == 10: # đi thẳng
        if i == 10:
            if A[i][j+1] == '.' and not visited[i][j+1]:
                added = False # đánh dấu xem danh sách có thêm mới gì vào không
                if xet: # sau khi đến đoạn đi thẳng ở đáy, cập nhât time
                    #listA = list_count
                    list_count.append((start,up_side_count))
                    added = True # có thêm mới
                    #new_list = [start,up_side_count]
                TF, list_ = quay_lui(i,j+1,0,-1,False,list_count,visited)
                if TF:
                    return True, list_
                if added:# trường hợp TF= False và đã thêm
                    list_count.pop()# khi quay lui cần phải xoá
                
        if i == 1:
            if A[i][j+1] == '.' and not visited[i][j+1]:
                if xet:
                    new_up = up_side_count+1
                    new_start =start
                TF,list_ = quay_lui(i,j+1,new_up,new_start,True,list_count,visited)
                if TF: # trường hợp TF= False-bị chặn và đã thêm
                    return True, list_
                
    if i < 10: # xuống
        if A[i+1][j+1] == '.' and not visited[i+1][j+1]:
            added = False # đánh dấu xem danh sách có thêm mới gì vào không
            if xet: # sau khi đến đoạn cần xuống, cập nhật time
                #listA = list_count
                list_count.append((start,up_side_count))
                added = True
                #new_list = [start,up_side_count]
            TF,list_ = quay_lui(i+1,j+1,0,-1,False,list_count,visited)
            if TF:
                return True, list_
            if added: # trường hợp TF= False và đã thêm
                list_count.pop() # khi quay lui cần phải xoá 
                
                
    if i>1: # lên
        if A[i-1][j+1] == '.' and not visited[i-1][j+1]:
            if xet: # nếu lên mà lên tiếp nghĩa là đang True thì đếm tiếp
                new_up = up_side_count+1
                new_start = start
            else: # lần đầu lên của đoạn lên mới nghĩa là đang False thì cặp nhật bắt đầu tại j và đếm bắt đầu =1
                new_up = 1
                new_start = j-1 #bắt đầu tại j-1 vì khởi tạo chạy từ 1 mà time lại bắt đầu tại 0
            TF,list_ = quay_lui(i-1,j+1,new_up,new_start,True,list_count,visited)
            if TF:
                return True,list_
    visited[i][j]== False
    return False, list_count
        

visited =[[False]*(n+1) for i in range(11)] # đánh dấu để quay lui không quay lại đi tiếp không đến chỗ vừa đi
TF,listA= quay_lui(10,1,0,-1,False,[],visited)
print(len(listA))
for x in listA:
    print(*x)
# 7 tham số:
# bắt đầu tại i,j
#số bước đang đi lên hoặc đi ngang
#điểm bắt đầu đi lên của đoạn đang cộng
# kiểm tra xem có đang đi lên không
# danh sách đoạn hợp lệ
#đánh dấu không đi tiếp đoạn đã đi















"""001
visited =[[False]*(n+1) for i in range(10+1)] # tranh đi lại đường cũ.
ans =[] # lưu kết quả.
pos =[] # lưu lại vị trí khi i==1 or i == 10

end = 0
start = 0

while j < n:
    visited[i][j] = True
    print('đầu','i','j',i,j)
    print(visited[i-1][j], visited[i-1][j+1])
    print(visited[i][j], visited[i][j+1])
    if i > 1 and i < 10:
        print(visited[i+1][j+1],visited[i+1][j+1])
    if i == 1 or i == 10: # điều kiện đi thẳng
        print(1)
        visited[i][j] = True
        pos.append([i,j])
        if i == 1:
            print(1.1)
            while  A[i][j+1] == '.' and not visited[i][j+1]:
                print(1.1,1)
                j+=1
                end +=1
                visited[i][j] = True
                if not visited[i][j]:
                    pos.append([i,j])
            if A[i][j+1] == 'X' and A[i+1][j+1] == '.' and not visited[i+1][j+1]: # nếu thẳng bị chăn và chéo xuống được.
                i+=1
                j+=1
            if A[i][j+1] == 'X' and A[i+1][j+1] == 'X': # nếu đường thằng và chéo xuống bị chăn.
                i,j = pos.pop()
            
                
        else:# i ==10:
            print(1.2)
            while  A[i][j+1] == '.' and not visited[i][j+1]:
                print(1.2,1)
                j+=1
                end +=1
                visited[i][j] = True
                if not visited[i][j]:
                    print('1.2,2')
                    pos.append([i,j])
            if A[i][j+1] == 'X' and A[i-1][j+1] == '.' and not visited[i+1][j+1]: # nếu thẳng bị chặn và chéo lên được.
                print('1.2.3')
                i-=1
                j+=1
            if A[i][j+1]=='X' and A[i-1][j+1]: # nếu chéo lên và thẳng bị chặn
                i,j = pos.pop()
        
        if 1 < i < 10: # điều kiện đi chéo
            if A[i-1][j+1] == '.' and not visited[i-1][j+1] and A[i+1][j+1] == '.' and not visited[i+1][j+1]: # trường hợp trong khoảng mà điểm đó có 2 hướng.
                    pos.append([i,j])
            print(2)
            if  (A[i+1][j+1] == '.' and not visited[i+1][j+1]) or (A[i+1][j+1] == '.' and not visited[i+1][j+1] and A[i-1][j+1] == 'X'):
                print(2.1)
                i+=1
                j+=1
                end +=1
                visited[i][j] = True
            if  (A[i-1][j+1] == '.' and not visited[i-1][j+1]) or (A[i-1][j+1] == '.' and not visited[i-1][j+1] and A[i+1][j+1] == 'X'):
                print(2.2)
                i-=1
                j+=1
                end +=1
                visited[i][j] = True
                print('i','j',i,j)
            if A[i+1][j+1] != '.' and A[i-1][j+1] != '.':
                print(3)
                i,j = pos.pop()
001"""
'''002
        if  (A[i+1][j+1] == '.' and not visited[i+1][j+1]) or (A[i+1][j+1] == '.' and not visited[i+1][j+1] and A[i-1][j+1] == 'X'):
            print(2.1)
            while (A[i+1][j+1] == '.' and not visited[i+1][j+1]):
                print(2,1,1)
                if A[i-1][j+1] == '.' and not visited[i-1][j+1] and A[i+1][j+1] == '.' and not visited[i+1][j+1]: # trường hợp trong khoảng mà điểm đó có 2 hướng.
                    pos.append([i,j])
                i+=1
                j+=1
                end +=1
                visited[i][j] = True
        if  (A[i-1][j+1] == '.' and not visited[i-1][j+1]) or (A[i+1][j+1] == '.' and not visited[i-1][j+1] and A[i+1][j+1] == 'X'):
            print(2.2)
            while (A[i+1][j+1] == '.' and not visited[i+1][j+1]):
                print(2,2.1)
                if A[i-1][j+1] == '.' and not visited[i-1][j+1] and A[i+1][j+1] == '.' and not visited[i+1][j+1]: # trường hợp trong khoảng mà điểm đó có 2 hướng.
                    pos.append([i,j])
                i-=1
                j+=1
                end +=1
                visited[i][j] = True
002'''

            
        
        
        

'''003
def quay_lui(i,j,visited):
    if j == n:
        return True
    visited[i][j] = True
    if (i==10 or i ==1):
        if A[i][j+1] == '.' and not visited[i][j+1]:
            if quay_lui(i,j+1,visited):
                return True
    if 1 < i < 10:
        if A[i-1][j+1] == '.' and not visited[i-1][j+1]:
            if quay_lui(i-1,j+1,visited):
                return True


        if A[i+1][j+1] == '.' and not visited[i+1][j+1]:
            if quay_lui(i+1,j+1,visited):
                return True
    return False
            
visited =[[False]*(n+1) for i in range(10+1)]

if A[10][1] == '.' and quay_lui(10,1,visited):
    print('có đường')
else:
    print('không có đường')
003'''



















