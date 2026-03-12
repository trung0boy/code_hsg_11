import sys
n,m = map(int,sys.stdin.readline().split())
A = [] # 3 tham số [khối lượng, giá trị, giá trị/1đơn vị khối lượng]
for i in range(n):
    wi,vi = map(int,sys.stdin.readline().split())
    A.append((wi,vi,vi/wi))

A.sort(key = lambda x: x[2]) # xắp xếp theo giá trị/đơn vị khới lượng.

ans = 0
for i in range(n-1,-1,-1):
    if m == 0:
        break
    if m >= A[i][0]:
        nK = m//A[i][0] # số lượng có thể lấy của vật đó
        ans += nK*A[i][1] # số lượng* giá trị của vật đó
        m %= A[i][0] # khối lượng còn lại
print(ans)
        
        
        























'''
5 15
12 4
2 2
1 1
1 2
4 10
'''
