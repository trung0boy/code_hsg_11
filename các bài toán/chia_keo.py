n,k = 9,3
a = [2,6,1,5,3,6,2,9,1]
m=n-k+1
w = [0]*(m+1)

for i in range(m+1):
    w[i] = sum(a[i:i+k])
for r in range ( i,m+1):
        

