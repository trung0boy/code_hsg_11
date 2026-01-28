#Sắp xếp lịch hội thảo (Activity Selection


n= int(input())
A=[]
for _ in range(n):
    A.append(list(map(int,input().split())))

count =0

end_time = 0
for i in range(n):
    if A[i][0] >= end_time:
        count+=1
        end_time = A[i][1]
print(count)
        




