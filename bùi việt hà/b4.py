"""
cho trước 1 dãy A tính chỉ số i
tướng ứng phần tử min của A
"""
'''

A=[3443,45,345,35,3432,432,63,2212,5623]
n=len(A)
f= min(list(range(n)), key = lambda i:A[i])
print(f)
'''
"""
tạo 1 dãy sinh ra all các số tự nhiên
"""
def all():
    i = 1
    while True:
        yield i
        i+=1
a = all()
for i in range(100):
    print(next(a))
"""
sinh 1 dãy tất cả số nfuyeen tố
"""

 
