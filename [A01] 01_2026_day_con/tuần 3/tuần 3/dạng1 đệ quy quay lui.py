#bài 1 sinh hoán vị của tập n
"""001
def backtrack(k):

    if k == n+1:
        print(res[1:])
        return
    for i in range (1,n+1):
        if not user[i]:
            res[k] = i
            user[i] =True
            backtrack(k+1)
            user[i] =False

n = int(input())
res = [0]*(n+1)
user = [False]*(n+1)
backtrack(1)
001"""

# bài 2 sinh tổ hợp với K phần tử
"""002
def sinh_to_hop (k):

    for i in range(res[k-1]+1, n - K + k +1):
        res[k] = i
        if k ==K:
            print(res[1:])
        else:
            sinh_to_hop (k+1)
            
n,K= map(int,input().split())
res=[0]*(K+1)
sinh_to_hop (1)
002"""

#bài toán xếp hậu

def n_queens(i):
    global count
    for j in range(1,n+1):
        if not cot[j] and not d1[i-j+n] and not d2[i+j]:
            res[i] = j
            cot[j] = d1[i-j+n] = d2[i+j] =True
            if i == n:
                count+=1
                print(res[1:])
            else:
                n_queens(i+1)
            cot[j] = d1[i-j+n] = d2[i+j] =False

n =int(input())
count=0
res = [0]*(n+1)
cot = [False]*(n+1)
d1 = [False]*(2*n+1)
d2 = [False]*(2*n+1)
n_queens(1)
print(count)







