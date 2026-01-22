
# =  = =

"""
BÀI 1: CẶP SỐ THÂN THIẾT (Tổng ước số)
Mô tả: Hai số nguyên dương a và b được gọi là "thân thiết" nếu tổng các ước thực sự (không kể chính nó) của số này bằng số kia.
        Ví dụ: 220 và 284 là cặp số thân thiết. Yêu cầu: Cho số N, hãy liệt kê tất cả các cặp số thân thiết (a,b) sao cho a<b≤N.
•	Input: Một số nguyên N (1≤N≤105).
•	Output: Mỗi dòng ghi một cặp số thân thiết.
•	Bộ Test:
o	Sample: 300 → Output: 220 284.
o	Test biên: 100 → Output: (Trống).
"""

#= = =
"""______________________________________
BÀI 2: TRUY VẤN SỐ NGUYÊN TỐ (Sàng Eratosthenes + Prefix Sum)
Mô tả: Cho Q truy vấn, mỗi truy vấn gồm hai số L,R.
        Hãy đếm xem có bao nhiêu số nguyên tố trong đoạn [L,R].
        Yêu cầu: Xử lý các truy vấn với tốc độ cực nhanh.
•	Input: Q≤105, 1≤L≤R≤106.
•	Output: Q dòng tương ứng với kết quả mỗi truy vấn.
•	Thuật toán: Dùng Sàng Eratosthenes để đánh dấu số nguyên tố, sau đó dùng Mảng cộng dồn để đếm số lượng.
"""
def eratosthenes(n):
    m=[True]*(n+1)
    m[0]=m[1]=False
    for i in range (2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j] = False
                return m
def prefic(n_max):
    m=eratosthenes(n_max)
    p=[0]*(n_max+1)
    for i in range(1,n_max+1):
        p[i] = p[i-1]+ (1 if m[i] else 0)
    #print(p)
def khoichay2():
    A=[]
    Q=int(input())
    for i in range(Q):
        L,R = map(int,input().split())
        A.append((L,R))
    print(A)
    p=prefic(max(max(A)))
    print(p)
    for L,R in A:
        print(p[R]-p[L-1])
    
#= = =
"""________________________________________
BÀI 3: PHÂN TÍCH THỪA SỐ NGUYÊN TỐ (Tối ưu hóa)
Mô tả: Một số nguyên N được phân tích dưới dạng N=p1a1⋅p2a2…pkak.
        Yêu cầu: In ra dạng phân tích đó theo định dạng chuẩn.
•	Input: N (2≤N≤1012).
•	Sample Input: 60 → Output: 2^2 * 3^1 * 5^1.
•	Sample Input: 100 → Output: 2^2 * 5^2.
•	Test Case: N là số nguyên tố lớn (1012+39).
"""


# = = =
"""________________________________________
BÀI 4: ƯỚC CHUNG LỚN NHẤT CỦA GIAI THỪA
Mô tả: Cho hai số n và m. Tìm ước chung lớn nhất của n! và m! (giai thừa).
        Yêu cầu: Giải bài toán với n,m rất lớn.
•	Input: Hai số n,m (1≤n,m≤1018).
•	Output: Một số duy nhất là kết quả của GCD(n!,m!).
•	Gợi ý: GCD(n!,m!)=min(n,m)!. Tuy nhiên, nếu kết quả quá lớn, đề bài thường yêu cầu chia dư cho 109+7.
•	Sample: 3 4 → Output: 6 (vì GCD(6,24)=6).
"""

#= = =
"""________________________________________
BÀI 5: SỐ PHẢN NGUYÊN TỐ (Antiprime Number)
Mô tả: Một số được gọi là "phản nguyên tố" nếu nó có số lượng ước số nhiều hơn bất kỳ số nguyên dương nào nhỏ hơn nó.
        Ví dụ: 1, 2, 4, 6, 12... Yêu cầu: Cho số N, tìm số phản nguyên tố lớn nhất không vượt quá N.
•	Input: N (1≤N≤109).
•	Output: Một số phản nguyên tố lớn nhất thỏa mãn.
•	Bộ Test: * Sample: 10 → Output: 6 (Số 6 có 4 ước: 1, 2, 3, 6; các số 1..5 có ít ước hơn).
o	Test lớn: 1000 → Output: 840.
"""







"""________________________________________
BÀI 6: SỐ ĐỐI XỨNG NGUYÊN TỐ (Palindromic Prime)
Mô tả: Tìm số nguyên tố P sao cho P cũng là một số đối xứng (đọc xuôi hay ngược đều giống nhau).
        Yêu cầu: Tìm tất cả các số đối xứng nguyên tố trong đoạn [A,B].
•	Input: 1≤A≤B≤107.
•	Sample: 5 150 → Output: 5, 7, 11, 101, 131.
"""














