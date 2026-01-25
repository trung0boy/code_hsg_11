#
import time

from collections import Counter

def tongchuso1(n): # tính tổng chữ số của n
    count=0
    while n > 0:
        count+= n%10
        n //=10
    return  count

def tongchuso2(n): # sưe dụng str
    return sum(int(i) for i in str(n))
    
star =time.time()

A=[12,23,23,23,23,30]
n=len(A)
#def tongtuongdong(n,A):
count=0
A_sum=[0]*n
for i in range(n):
    A_sum[i] = tongchuso2(A[i])
B_sum = Counter(A_sum)
#print(B_sum)
for i in B_sum:
    if B_sum[i] >=2:
        count+=(B_sum[i]*(B_sum[i]-1))//2
print(count)
end = time.time()
print(end-star)
    
        
    
