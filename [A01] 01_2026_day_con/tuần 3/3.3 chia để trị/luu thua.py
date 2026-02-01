def luu_thua(a,n,m):
    if n==0:
        return 1
    an = luu_thua(a,n//2,m) # chia đôi ra cho đến khi n chỉ còn là 0 khi đó a^0 =1
    if n%2==0: # tính modM của số nhỏ hơn 10 -> 5 -> 2 -> 1 -> 0
        return (an*an)%m # nếu n chẵn
    else:
        return(a*an*an)%m # nếu n lẻ
    
    

a,n,m = map(int,input().split())
print(luu_thua(a,n,m))
