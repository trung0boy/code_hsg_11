
def quick_sort(A,k):
    if len(A)<=1:
        return A
    else:
        p = A[len(A)//2]
        L = [ i for i in A if i > p]
        G = [ i for i in A if i == p]
        R = [ i for i in A if i < p]

    if k <= len(L):
        return quick_sort(L,k)
    if len(L) < k < len(L)+len(G):
        return quick_sort(L,k) +G
    if k >= len(L) +len(G):
        return quick_sort(L,k) + G + quick_sort(R,k)
    return

A = [3, 2, 1,5,4]
k=2

ans = quick_sort(A,k)
print(ans,ans[k-1])
