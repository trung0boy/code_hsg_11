import sys
n,c = map(int,sys.stdin.readline().split())
A=[]
for i in range(n):
    ai,bi = map(int,sys.stdin.readline().split())
    A.append((ai,bi))

A.sort(key = lambda x:x[0])

ans = 0
for x in A:
    if c >= x[0]:
        ans += 1
        c+= x[1]
    else:
        print(ans)
        break
        
        
