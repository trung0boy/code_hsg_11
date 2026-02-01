def tinh(i,j):
    return ( ( ( j[0] - i[0] )**2)  + (( j[1] - i[1])**2 ))**0.5

def closet(l,r):
    print(l,r)
    if 0< r-l <= 2:
        dm = float('inf')
        for i in range(l,r):
            for j in range(i+1,r+1):
               dm = min(dm, tinh(A[i],A[j]))
            return dm

    global d
    mid = (l+r)//2
    li =  closet(l,mid)
    ri =  closet(mid+1,r)
    d = min(d,li,ri)
    print('m',li,ri,mid)

    mid_x=A[mid][0]

    strip=[A[i] for i in range(l,r) if abs(A[i][0] - mid_x) < d]
    print('s',strip)
    for i in range(len(strip)-1):
        for j in range(i+1,len(strip)):
            d = min(d,tinh(strip[i],strip[j]))
    return d

d=float('inf')
n = int(input())
A=[]
for i in range(n):
    A.append(list(map(int,input().split())))
A.sort( key = lambda x:x[0])
print(A)
kq = closet(0,n-1)
print(kq)
        
