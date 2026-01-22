
'''001
#Dạng 1: Thuật toán Quay lui (Backtracking)
def backtrack(k):
    if k == n+1:
        print(res[1:])
        return
    for i in range(1,n+1):
        if not user[i]:
            res[k]=i
            user[i] = True
            backtrack(k+1)
            user[i] = False
    

n=int(input())
res=[0]*(n+1)
user=[False]*(n+1)
backtrack(1)
001'''

#Bài 2: Bài toán Tổ hợp (Sinh tập con K phần tử)
#Đề bài: Cho tập hợp {1,2,...,N}. Liệt kê tất cả các tập con có đúng K phần tử.
#Thuật toán: Để tránh trùng lặp, ta quy định các
#phần tử trong tập con phải được chọn theo thứ tự tăng dần (x[k]>x[k−1]).
#Giới hạn chọn: Phần tử thứ k (x[k])
#có giá trị nhỏ nhất là x[k−1]+1 và lớn nhất là N−K+k.


def to_hop(k):
    for i in range(res[k-1]+1, n - K + k+1):
        res[k] = i
        if k==K:
            print(res[1:])
            return
        else:
            to_hop(k+1)


n,K = map(int,input().split())
res = [0]*(K+1)

to_hop(1)

































