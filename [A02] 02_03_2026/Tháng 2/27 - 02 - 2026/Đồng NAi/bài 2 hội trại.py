import sys

N = sys.stdin.readline()

pos_N = {'0','1','2','3','4','5','6','7','8','9'}
ans = 0
n = 0
for i in N:
    if i in pos_N:
        n = (n*10) + int(i)
    else:
        ans += n
        n = 0
print(ans)
