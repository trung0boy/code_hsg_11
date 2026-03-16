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



'''
Test case #1:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #2:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #3:	AC	[0,022s,	11,13 MB]	(1/1)
Test case #4:	AC	[0,023s,	10,88 MB]	(1/1)
Test case #5:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #6:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #7:	AC	[0,022s,	11,00 MB]	(1/1)
Test case #8:	AC	[0,024s,	12,00 MB]	(1/1)
Test case #9:	AC	[0,089s,	117,27 MB]	(1/1)
Test case #10:	AC	[0,089s,	118,04 MB]	(1/1)
'''
