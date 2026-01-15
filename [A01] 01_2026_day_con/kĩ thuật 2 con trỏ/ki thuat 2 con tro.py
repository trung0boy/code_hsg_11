from collections import Counter
import sys
input = sys.stdin.readline


'''
Bài 1: Đếm số cặp có tổng không vượt quá K
Đề bài: Cho dãy A gồm N phần tử đã sắp xếp tăng dần và số K. Đếm số cặp (i,j) với i<j sao cho A[i]+A[j]≤K.
'''


def ans_sum():
    A=[2,2,3,4,6,6,9,10,11,    15,18,19]
    
    n=12
    k=13

    l=0
    r=n-1

    ans = 0  #tong so cap

    while l<r:
        if A[l] + A[r] <= k:
            ans += (r-l)
            l+=1
            
            print("a",A[l:r])
        else :
            r-=1

        print(ans)



'''
Bài 2: Đoạn con ngắn nhất có tổng ≥S
Đề bài: Cho dãy số nguyên dương A và số S.
Tìm độ dài của đoạn con liên tiếp ngắn nhất có tổng các phần tử
lớn hơn hoặc bằng S.
'''


def shortest_subarray():
    #  0 1 2 3 4 5 6 7 8  9 10 11 12
    A=[6,3,9,6,6,2,7,6,2,12,13,8, 3, 3]
    S=12
    n=len(A)

    l=0
    curr_sum = 0
    min_len = float('inf')

    for r in range(n):
        curr_sum +=A[r]
        while curr_sum >= S:
            min_len= min(min_len,r-l+1)
            curr_sum-=A[l]
            l+=1
    if min_len == float('inf'):
        print(0)
    else:
        print(min_len)
        
'''
Tìm bộ ba số có tổng bằng S (3-Sum)
Đề bài: Cho mảng A và số S. Tìm ba chỉ số i,j,k khác nhau sao cho A[i]+A[j]+A[k]=S.

'''

def three_sum():
    A=[1,3,2,4,6,7,8,10,11,12,15]
    S=12
    n=len(A)

    for i in range (n-2):
        l,r = i+1, n-1

        k = S-A[i]
        while l<r:
            if A[l]+A[r] == k:
                print(A[i], A[l], A[r])
                return
            elif A[l]+A[r] < k:
                l+=1
            else:
                r-=1
        print('0')


'''
Bài 3: Đếm số cặp có hiệu A[j]−A[i]=K
Mục tiêu: Sử dụng kỹ thuật Hai con trỏ cùng chiều trên mảng đã sắp xếp.
•	Thuật toán:
o	Vì mảng đã sắp xếp, khi tăng j thì hiệu A[j]−A[i] tăng, khi tăng i thì hiệu giảm.
o	Ta dùng hai con trỏ i và j. Với mỗi i, ta tăng j cho đến khi A[j]−A[i]≥K.
o	Nếu A[j]−A[i]==K, ta đếm số lượng phần tử bằng A[j] và A[i]
    (trường hợp mảng có các phần tử trùng nhau). Nếu mảng các phần tử phân biệt, chỉ cần ans += 1.
•	Bộ Test mẫu:
o	Input:
o	6 2
o	1 2 3 3 4 5
o	Giải thích: Các cặp là: (1, 3), (1, 3), (2, 4), (3, 5), (3, 5).
o	Output: 5
'''             
def counter_dis():
    n,k = 6,2
    A=[1,2,3,3,4,5] 
    cA=Counter(A) #{value:tan xuat}
    ans=0 #luu so luong
    print(cA)
    if k==0:
        for i in cA:
            if cA[i] >1:
                ans += (cA[i]*(cA[i]-1)) / 2
    else:
        for i in cA:
            if i + k in cA:
                ans += cA[i]*cA[i+k]
    print(ans)
                




















