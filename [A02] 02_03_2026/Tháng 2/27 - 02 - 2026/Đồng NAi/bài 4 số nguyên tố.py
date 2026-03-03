import sys

def tach(n):
    s = 0
    while n != 0:
        s += n%10
        n//=10
    return s

def nguyen_to_LR(l,r):
    ans = 0
    m =[True]*(r+1)
    m[0] = m[1] = False
    for i in range(2,int(r**0.5)+1):
        if m[i]:
            for j in range(i*i,r+1,i):
                m[j] = False
    for i in range(l,r+1):
        if m[i]:
            ans += tach(i)
    return ans


l,r = map(int,sys.stdin.readline().split())
print(nguyen_to_LR(l,r))
