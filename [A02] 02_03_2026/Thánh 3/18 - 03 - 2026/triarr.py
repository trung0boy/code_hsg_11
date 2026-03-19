import sys
import math
from collections import *

n,m = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

cnt = {}
for x in A: # tính ước của mỗi số
    g = math.gcd(x,m)
    cnt[g] = cnt.get(g,0)+1 # đếm ước.

ans = 0
for i in cnt: # tổ hợp có lặp lại
    for j in cnt:
        for k in cnt:
            if math.gcd(i*j*k)%m==0: # tích i,j,k =0(ModM).
                ans += cnt[i]*cnt[j]*cnt[k] # tích số lượng.
print(ans)
    
