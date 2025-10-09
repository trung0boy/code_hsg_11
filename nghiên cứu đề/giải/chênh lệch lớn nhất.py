


n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
res=0
for i in range(n):
    mxA=0               # GT lớn nhất của A[k+1] - A[k]
    for j in range(i,n):
        if j != i:
            mxA = max(mxA, abs(a[j] - a[j-1]) )
        for u in range(n):
            mxB =0           # GT lớn nhất của B[k+1] - B[k]
            for v in range(u,n):
                if u != v:
                    mxB = max(mxB, abs(b[v] - b[v-1]) )
                if (j-i+1)+(v-u+1)==m and a[j] <  b[u] :
                    res = max(res, mxA, mxB, abs(a[j] - b[u]))
    print(res)
#j-i+1 độ dài của dãy A
#v-u+1 độ dài của dãy B 
# sao cho độ dài của dãy A+B = m
 
