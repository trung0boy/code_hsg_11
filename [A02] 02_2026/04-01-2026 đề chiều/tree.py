
def eratosthene(n):
    m=[True]*(n+1)
    m[0] = m[1] = False
    for i in range(2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j] = False
    return [i for i in range(1,n+1) if m[i]]


n = int(input())
tree = list(map(int,input().split()))

A =sorted(tree,reverse=True) # sắp xếp và đảo ngược
m = eratosthene(A[0]) #max

pos = []
leght = 0
for i in A:
    if i in m:
        if leght%2==0:
            pos.append(i)
            leght+=1
        else:
            pos.insert(0,i)
            leght+=1
if len(pos)==0:
    print(-1)
else:
    print(*pos)

