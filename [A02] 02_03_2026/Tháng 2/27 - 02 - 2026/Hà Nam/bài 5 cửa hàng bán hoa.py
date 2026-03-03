import sys
from collections import deque
import numpy # hàm này xử lí với list cực nhanh
n,m =map(int, sys.stdin.readline().split())
A = []
F =[]
S=[]

for i in range(n):
    f,s = map(int, sys.stdin.readline().split())
    F.append(f)
    S.append(s)

l =0
sum_val =0
ans = float('inf')
pos = deque()
 # áp dụng string window
for r in range(n):
    
    sum_val += F[r] # tổng liên tiếp
    pos.append(S[r])

    while sum_val >= m: # trong đoạn khi thảo mãn tổng giá trị
        ans = min(ans, numpy.amax(pos)) # chiều cao nhỏ nhất của các chiều cao lớn nhất đã lấy các đoạn
        sum_val -= F[l] # thu nhỏ lại
        if pos:
            pos.popleft() # xoá để thu nhỏ
        l+=1
        
print(int(ans))
