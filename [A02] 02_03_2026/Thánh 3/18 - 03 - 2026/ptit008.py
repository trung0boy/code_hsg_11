import sys
n,m = map(int,sys.stdin.readline().split())

a=[]
for _  in range(m):
    d,val  = map(int,sys.stdin.readline().split())
    a.append((d,val))


for i in range(1,m):
    d1,h1 = a[i-1]
    d2,h2 = a[i]
    if abs(h1-h2) > d2 - d1:
        print(-1)
        exit()
ans = 0


d,h = a[0]
ans = max(ans, h + (d-1))
for i in range(1,m):
    d1,h1=a[i-1]
    d2,h2= a[i]
    điff = abs(h1-h2)
    leght = d2 - d1

    cnt =max(h1,h2) + (leght - diff)//2
    ans = max(ans,cnt)

d,h = a[-1]
ans = max(ans,h - (n-d))
print(ans)
    
