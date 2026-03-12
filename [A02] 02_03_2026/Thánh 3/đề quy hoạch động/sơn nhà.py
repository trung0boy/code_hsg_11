import sys
sys.stdin = open('sơn nhà.txt','r')
input = sys.stdin.readline

n = int(sys.stdin.readline())
A=[]
for i in range(n):
    ri,gi,bi = map(int,sys.stdin.readline().split())
    A.append((ri,gi,bi))

dp =[[0]*3 for i in range(n)] # chứa 3 giá trị ri,gi,bi

for i in range(n):
    ri, gi, bi = A[i]
    dp[i][0] = min(ri  + dp[i-1][1],   ri + dp[i-1][2]) #ri
    dp[i][1] = min(gi + dp[i-1][0],   gi + dp[i-1][2]) #gr
    dp[i][2] = min(bi + dp[i-1][0],   bi + dp[i-1][1]) #bi

print(min(dp[-1]))
"""
phương án với mỗi 1 màu sẽ cặp nhật tổng nhỏ nhất khác màu trước đó + màu hiện thời:
    
dp[0] = min(ri + dp[i-1][1],   ri + dp[i-1][2])
dp[1] = min(ri + dp[i-1][0],   ri + dp[i-1][2])
dp[2] = min(ri + dp[i-1][0],   ri + dp[i-1][1])

kết quả là 3 giá trị ở cuối cùng:
min(dp[-][0], dp[-][1], dp[-][2])
"""
