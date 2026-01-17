def bresic_sum(A,n):
    p=[0]*(n+1)
    p[0]=A[0]
    for i in range(n):
        p[i] = p[i-1] + A[i]
    return p



"""001
dạng 4: kết hợp Kỹ thuật sliding window
bài toán: cho dãy A và số K. tìm đoạn con liên tiếp có độ dài
đúng bằng K sao cho tổng của chúng là lớn nhất.
001"""

#A=[2,1,5,1,3,2,8,4,1]
A=[4,2,-1,0,3,-2,5,-3,6]
#A=[1,2,1,2,2,1,2,3,4,2,2,1]


p=bresic_sum(A,len(A))
k=3

leng = 0
max_sum = 0
for i in range(k,len(A)):
    # max_sum =max(max_sum, p[i]-p[i-k] # nếu chỉ cần max
    leng = p[i]-p[i-k]
    if leng > max_sum:
        max_sum = leng
        j=i
print(max_sum)
print(A[j-k+1:j+1])
    
    


































