import sys
n = int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
A.append(min(A))
ans =1
count=1
for i in range(1,n):
    if A[i]>=A[i-1]:
        count+=1
        print(count)
    else:
        ans = max(ans,count)
        count=1
print(ans)
    
