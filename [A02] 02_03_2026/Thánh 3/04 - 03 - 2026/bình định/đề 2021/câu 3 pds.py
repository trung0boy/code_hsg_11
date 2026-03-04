import sys

def tach(n):
    tong = 0
    tich = 1
    while n>0:
        s = n%10
        tong += s
        tich *= s
        n//=10
    return (tich%tong)==0



n = int(sys.stdin.readline())
i = 1

while n > 0:
    if tach(i):
        n-=1
    i+=1
print(i-1)
    


































