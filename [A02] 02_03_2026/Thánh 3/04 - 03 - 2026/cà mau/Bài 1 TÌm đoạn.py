import sys
import random
import time

def randomA(A):
    A=[]
    for i in range(n):
        A.append(random.randint(1,1000000000))
    #n1 = random.randint(1,n-5)
    return A
                 
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

#n=1000
#A=randomA(n)


start = time.time()
def for_j(A,i,ans):
    curr = 0
    for j in range(i-1,n):
        curr += A[j]
        if curr == 2021: # nếu bằng số nhỏ nhất thì đó là min luân
            return curr
        if curr > ans: # nếu lớn hơn min hiện tại thoạt luân
            return ans
        if curr > 2021 and curr < ans and curr%2021==0: # nếu nhỏ hơn min hiện tại và lớn hơn yêu cầu
            return curr
    return ans
            
ans = float('inf')
for i in range(n):
    min_ans = min(ans,for_j(A,i,ans))
    ans = min(ans,min_ans)
    
    if ans == 2021:
        print(ans)
        end1 = time.time()
        print(end1 - start)
        sys.exit()
        
end2 = time.time()
print(end2 - start)
print(ans)
        





























'''
def boi_2021():
    A = []
    for i in range(1,2021+1):
        if 2021%i == 0:
            A.append(i)
    return A
pos = boi_2021()
ans = float('inf')
for i in range(n):
    curr = 0
    j = i
    while curr <= 2021 and j > -1:
        curr += A[j]
        if curr in pos:
            ans = min(ans,curr)
        j-=1
print(ans)
'''
        
