import sys
import random
import time

def randomA(n):
    A=[]
    for i in range(n):
        A.append(random.randint(1,100))
    return A


def hai_so(n,A):
    
    if len(set(A)) <= 2:
        return n

    l = 0
    r = 1
    ans = 0
    while r < n:
        while len(set(A[l:r+1])) > 2:
            l += 1
            continue
        ans = max(ans,r-l+1)
        #print("l-r",r-l+1)
        #print("ans",ans)
        r += 1
    return ans


n = 1000000
A = randomA(n)

start = time.time()

b = hai_so(n,A) # logic

end = time.time()
print('xong',end - start)

#n = int(sys.stdin.readline())
#A = list(map(int,sys.stdin.readline().split()))

#print(hai_so(n,A))



