
n, k = map(int, input().split())
A=list(map(int,input().split()))

res =[False]*(k+1)
res[0] =True
for i in A:
    for j in range(k, i-1,-1):
        if res[j - i]:
            res[j] = True
        print(res, i ,j)
print ('y' if res[k] else 'n')
            
    
