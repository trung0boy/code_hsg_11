import sys
sys.setrecursionlimit(10**5)
#sys.stdin = open('dpsteps fibo.txt','r')
#input = sys.stdin.readline


n ,m= map(int,sys.stdin.readline().split())
A = set(list(map(int,sys.stdin.readline().split())))

fib = [0]*(n+2)
fib[0]=1

for i in range(1,n+2):
    if i in A:
        fib[i]=0
    else:
        fib[i] = fib[i-1]
        if i>=2:# vì nếu nhỏ hơn 2 sẽ không cộng được i-2
            fib[i] += fib[i-2]
print(fib[n]%1000000007)
