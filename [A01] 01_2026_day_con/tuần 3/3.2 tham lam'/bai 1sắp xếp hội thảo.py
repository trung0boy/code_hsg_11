#Sắp xếp lịch hội thảo (Activity Selection


n= int(input())
A=[]
for _ in range(n):
    A.append(list(map(int,input().split())))
A.sort(key = lambda x:x[1]) # sắp xếp theo thời gian kết thúc

count =0

end_time = 0  #lưu thời gian kết thúc của cuộc hội thảo trước đó
for i in range(n):
    if A[i][0] >= end_time:
        count+=1
        end_time = A[i][1]
print(count)
        

