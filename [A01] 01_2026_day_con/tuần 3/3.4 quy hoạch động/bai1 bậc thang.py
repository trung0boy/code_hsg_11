import time


# fi = fi-1 + fi-2 + fi-3
# khi i đến c=bậc bị hỏng gán i tại đó =0

def bac_thang(n,A):
    st = time.time()
    setA = set(A)
    x0 , x1 , x2 = 1,0,0 #i-3, i-2, i-1
    
    for i in range(n+1):
        if i in setA: # nếu bậc hỏng là không có đường lên bặc đó
            xi =0
        else:
            xi = (x0+x1+x2)% (10**6+7)
        x0,x1,x2 = x1,x2,xi # đẩy kết quả đã tính xuống 1 bặc
        print(x0,x1,x2,xi)
            
    ed = time.time()
    print(x2)
    print(ed - st)
    
       
n ,m = map(int,input().split())
A=list(map(int,input().split()))

bac_thang(n,A)
