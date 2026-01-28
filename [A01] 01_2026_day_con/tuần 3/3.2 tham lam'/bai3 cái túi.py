

    
        

n, value_max = map(int,input().split())
Ag = []
for i in range(n):
    Ag.append(list(map(int,input().split())))


A = []  
for w,v in Ag:
    dongia = v/w
    A.append((w,dongia))  
A.sort(key = lambda x: x[1])
A.reverse()


ans = 0 # tổng số tiền
Wi = value_max # khối lượng đang xét
for i in range(n):
    if A[i][0] <= Wi:
        ans += A[i][0]*A[i][1]
        Wi -= A[i][0]
    else:
        ans += A[i][1]*Wi
        
print(ans)
        
