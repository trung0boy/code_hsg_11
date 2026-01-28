
def vali(k):
    if k == n+1:
        print(A[1:])
        return
    for i in range(1,m+1):
        if A[k-1] == i: # tránh trường hợp trùng số liên tiếp
            continue
        A[k] = i
        vali(k+1)


n,m =map(int,input().split())
A=[0]*(n+1)
vali(1)
