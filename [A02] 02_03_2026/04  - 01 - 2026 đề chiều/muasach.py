import time
import random
'''
k=10000
n =1000000
A = []
for i in range(n):
    A.append(random.randint(1,100000000))
'''



def mua_sach(n,k,A):
    A.sort()
    l = 0
    r = n-1
    Max = 0
    while l<r-Max+1:
        count = 0
        i=l
        while A[i] - A[l] <= k:
            count+=1
            i+=1
        Max = max(Max,count)
        l+=1
    return Max

n,k = map(int,input().split())
A = list(map(int,input().split()))
start = time.time()           
ans=mua_sach(n,k,A)

end = time.time()
print(ans,end-start)
