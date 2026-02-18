#A = [3,4,1,6,7,7]
#A= [1,2,3,4,5]
#A=[3,3,4,5,2,6,1]
A=[1,2,1,2,1,2,1,2,1,2]
n = len(A)
dp = [0]*(n+1)

for i in range(len(A)-1,-1,-1):
    dp[i] = dp[i+1] # xoá
    if i +A[i] < n: # hoặc chọn làm mốc
        dp[i] = max(dp[i], A[i]+1 + dp[i +A[i]+1])
print(dp)
print(n - dp[0])
