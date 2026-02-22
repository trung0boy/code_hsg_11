import math

#dạng 2
# tìm cặp (a,b) khi biết G-gcd và L-lcm
'''
a.b = g//l
đặt
a=G.x
b=G.y
khi đó: x.y = G//L và gcd(x,y)==1
'''
import math
def slove(G,L):
    if L%G != 0: # để TM cần l%G phải không dư
        return []
    xy = L//G # tích 2 ẩn
    res=[]
    for x in range(1,int(xy**0.5)+1): 
        if xy % x == 0 : 
            y = xy // x
            if math.gcd(x,y)==1: # bội chung của hai số phải bằng 1
                res.append((G*x,G*y))
    return res


# rút gọn phân số
# chia cả tử và mẫu cho gcd
def rut_gon_phan_so(a,b):
    g = math.gcd(a,b)
    
    return a//g, b//g


# tìm số cặp Gcd(a,b)=k và a+b =S
# a+b =S suy ra b = S-a
# kiểm tra xem trong b có tồn tạo trong đoạn A[i::] không
# nếu tồn tại, mang kiểm tra gcd


def so_cap_tm(A,K,S):
    d=[]
    for i in range(len(A)):
        if S - A[i] in A[i::]:
            if math.gcd(A[i], S-A[i]) == K:
                d.append((A[i],S-A[i]))
                        
    return d
        



def analyze_n(n):  # phân tích thừa số nguyên tố và đếm ước
    d_count = 1 # số lượng ước
    s_sum = 1 # tổng ước
    i = 2
    temp = n
    while i*i <= temp:
        p_pow =0
        p_sum =1
        p_val = 1
        while i%n==0:
            p_pow += 1
            p_val *= i
            p_sum += p_val
            temp //= i
        d_count *= (p_pow+1)
        s_sum *= p_sum
    i+=1
    if temp>1:
        d_count *=2
        s_sum *= (1+temp)
    return d_count, s_sum
        




def tim(G,L):
    if L%L !=: return False
    xy = L//G
    res = []
    for x in range(1,int(xy*0.5)+1):
        if xy%x == 0:
            y = xy%x
            if math.gcd(x,y) ==1:
                res.append((G*x,G*y))
    return res













    

