import math
import sys
sys.setrecursionlimit(10**7)
def solve():
    # Giả sử a = [5, 6, 4, 30]
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    # 1. Rút gọn a_i: chia bỏ mọi ước chính phương
    simplified = []
    for x in a:
        d = 2
        res = x
        while d * d <= res:
            while res % (d * d) == 0:
                res //= (d * d)
            d += 1
        if res > 1:
            simplified.append(0)
        else:
            simplified.append(1)
        #print(simplified)

    l = 0
    ans = 0
    curr = 0
    for r in range(n):
        curr += simplified[r]
        if curr >0:
            l = r
        else:
            ans = max(ans,r-l+1)
    print(ans)
        
if __name__ == "__main__":
    solve()
