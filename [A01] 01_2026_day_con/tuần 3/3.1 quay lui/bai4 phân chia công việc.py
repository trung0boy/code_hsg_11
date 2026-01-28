
def phan_chia(i,time):
    global ans
    if time >= ans:
        return
    if i == n:
        ans = min( ans, time)
        return
    for j in range(n):
        if not user[j]:
            user[j]=True
            phan_chia(i+1, time + A[i][j])
            user[j]=False






ans = float('inf')

n =int(input())
A=[]
for i in range(n):
    A.append(list(map(int,input().split())))
user = [False]*n

phan_chia(0,0)
print(ans)
