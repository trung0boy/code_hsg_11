n,S = map(int,input().split())
A = list(map(int,input().split()))
B = [0]*n
i = 0
while sum(B) < S:
    if i > n-1:
        i =0
    if sum(B) < S and B[i] < A[i]:
        B[i]+=1
    i+=1
print(B)

