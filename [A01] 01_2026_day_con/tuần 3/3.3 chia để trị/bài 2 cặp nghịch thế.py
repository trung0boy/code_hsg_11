def nghich_the(A):
    if len(A)<=1:
        return A
    mid =len(A)//2

    L = A[:mid]
    R = A[mid:]

    L_s, inL = nghich_the(L)
    R_s,inR = nghich_the(R)
    count = inL+inR
    
    i = 0
    j = 0

    pos = []
    while i< len(L_s) and j < len(R_s):
        if L_s[i] <= R_s[j]:
            pos.append(L_s[i])
            i+=1
        else:
            pos.append(R_s)
            count+=len(R_s)-i
            j+=1
    pos.extend([i:])
    pos.extend([:i])
    return pos, count
            
    


n = int(input())
A = list(map(int,input().split()))
a,b =  nghich_the(A)
