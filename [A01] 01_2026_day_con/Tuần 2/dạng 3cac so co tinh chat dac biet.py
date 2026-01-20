#dạng 3
# hàm này dùng để tách chữ số
#vd: n=1234 -> [4,3,2,1]
def tach_chu_so(n): # cách 1
    ds=[]
    while n>0:
        ds.append(n%10)
        n//=10
    return ds

# hoặc cách 2 nếu n nhỏ
nts =1234
dus = [i for i in str(nts)]

#= = =


# kiểm tra xem n có phải số cính phương không 
def is_square(n):
    if n < 0:
        return False
    k = int(n**0.5)
    return k*k == n # True/False


# số đối xứng
#là số khi đọc theo chiều nào vẫn là chính nó vd 121, 123321,...

def is_palindrome1(n): # cách 1
    s=str(n)
    return s == s[::-1]
def is_palindrome2(n): # toán học
    tmp = n
    rev = 0
    while n > 0:
        rev = rev*10 + n%10 # nhân 10 để tăng thêm độ dài và công với phần dư của n
        n //= 10 # bỏ dư
    return rev == tmp


# số hoàn hảo
#tổng các ước thực sự bằng chính nó

def is_perfect(n):
    if n<= 1:
        return False
    S=1
    i=2
    while i*i <=n:
        if n%i == 0:
            S+=i
            if i != n//i:
                S+= n//i
        i+=1
    return S

#4. SỐ ARMSTRONG (SỐ MẠNH)
#📌 Định nghĩa

#Tổng các chữ số mũ k (k = số chữ số) = chính nó
#vd 153 = 1³ + 5³ + 3³


#Ý tưởng
#đếm số chữ số
#Tách chữ số
#Tính tổng lũy thừa

def is_armstrong(n):
    d=[]
    tmp = n
    while tmp > 0:
        d.append(tmp%10)
        tmp//=10
    k=len(d)
    S=0
    for i in d:
        S += i**k
    return S==n
        






























