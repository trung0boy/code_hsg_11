


D,G,N = list(map(int,input().split())) # khoảng cách AB, số km đi đc, số trạm xăng trên tuyến AB
A = list(map(int,input().split()))
A.append(D)
n =len(A)

i = 0
curr = 0
count =0

while curr + G <100:
    last = curr
    while i < n and A[i] < curr +G:
        last = A[i]
        i+=1
    if last ==curr:
        print(-1)
    count+=1
    curr = last
    
print(count)
