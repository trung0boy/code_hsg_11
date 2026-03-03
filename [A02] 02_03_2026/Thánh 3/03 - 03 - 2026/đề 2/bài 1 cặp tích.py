import sys
import random
import time


def randomA(n):
    A=[]
    for i in range(n):
        A.append(random.randint(1,1000000))
    return A

#n = int(sys.stdin.readline())
#A =list(map(int,input().split()))

n=1000000
A = randomA(n)


count_chan = 0

count_le = 0

s = time.time()
for x in A:
    if x%2 == 0:
        count_chan +=1
    else:
        count_le += 1
#ans_chan = (count_chan*(count_chan-1))
ans_n = (n*(n-1))//2
ans_le = (count_le*(count_le - 1))//2
e = time.time()
print(e -s)
print(ans_n - ans_le) # tổng biến cố xảy ra - biến cố đối
