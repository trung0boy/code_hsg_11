import sys

'''
#
def tach_tong_one(n):
    if n < 10:
        return n

            
    temp = n
    ans = 0
    while temp > 0:
        ans = ans + temp%10
        temp//=10
    return tach_tong_one(ans)


q = int(sys.stdin.readline())

for i in range(q):
    l,r = map(int,sys.stdin.readline().split())
    ans=0
    for j in range(l,r+1):
        ans += tach_tong_one(j)

    print(ans)
        
'''
def nmod9(a):
    if a == 0:
        return 0
    n = a//9
    k = a%9
    
    ans = (45 * n) + ((k * (k+1)) // 2)
    #print(n,k,ans)
    return ans
q = int(sys.stdin.readline())

for i in range(q):
    l,r = map(int,sys.stdin.readline().split())
    print(nmod9(r) - nmod9(l-1))
    
'''
quy luật luân lặp lại từ 1 đến 9: 45

nmod9
công thức
45 * (n/2) + (k(*k+1)//2)
k là dư
'''




















