'''
trương trình này
nếu dùng cho n <= 3.10^6 thì hoạt động tốt
'''




import time
import sys
input = sys.stdin.readline


def eratosthene(n): # sàng gốc
    m=[True]*(n+1)
    m[0]=m[1]=False
    for i in range(2,int(n**0.5)+1):
        if m[i]:
            for j in range(i*i,n+1,i):
                m[j] = False
    return [i for i in range(n) if m[i]]

# = = =
def spf_primes(n): #gán bội của nguyên tố thành nguyên tố nhỏ nhất
    fps=[0]*(n+1)
    for i in range(2,n+1):
        if fps[i] == 0:
            fps[i]=i
            for j in range(i*i,n+1,i):
                if fps[j]==0:
                    fps[j] = i
    return fps

def factorzize(n):  # phân tích thừa số
    #start = time.time()
    pos = {}
    spf = spf_primes(n)
    while n > 1:
        p = spf[n]
        pos[p] = pos.get(p,0)+1
        n//=p
    #end = time.time()
    #print(end - start)
    print('*'.join(f'{k}^{v}'for k,v in pos.items()))
    return

N = int(input())
factorzize(N)
