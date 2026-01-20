
#Dạng 5: Chữ số và Cơ số (Tách số)
#Bài toán: Cho số N. Kiểm tra N có phải là số "Đặc biệt"
#(tổng các chữ số là số nguyên tố).
#Kỹ thuật: Tách chữ số bằng toán học để nhanh hơn ép kiểu xâu.


def is_primes(n): # kiểm tra nguyên số
    if n < 2:return False
    
    
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def sum_dis(n): # tách và tổng lại
    s=0
    while n > 0:
        s += n%10
        n//=10
    return s
        
def kiemtra_prime_sum(n):
    if is_primes(sum_dis(n)):
        return 'đặc biệt'
    else:
        return 'không đặc biệt'
    
#5.1
'''
    Số siêu nguyên tố (Super Prime)
Thuật toán: Thay vì kiểm tra từng số xem có phải siêu nguyên tố không (rất chậm), ta dùng phương pháp Loang (BFS) hoặc Đệ quy (DFS) để "xây dựng" số siêu nguyên tố từ trái sang phải.
Bắt đầu với các số nguyên tố có 1 chữ số: 2, 3, 5, 7.
Với mỗi số đã có, ta thử thêm một chữ số lẻ {1, 3, 7, 9} vào bên phải.
Nếu số mới tạo thành là số nguyên tố, ta tiếp tục quá trình cho đến khi đạt được số chữ số yêu cầu.
'''

def sieu_nguyen_to(number, leght, n='do_dai_yeu_cau'):
    if leght == n:
        print(number)
        return
    for i in [1,3,5,7,9]:
        next_number = number*10 + i
        if is_primes(next_number):
            sieu_nguyen_to(next_number, leght+1, n)
            
def sinh(n):
    for star in [2,3,5,7]:
         return(sieu_nguyen_to(star, 1, n))
    







































