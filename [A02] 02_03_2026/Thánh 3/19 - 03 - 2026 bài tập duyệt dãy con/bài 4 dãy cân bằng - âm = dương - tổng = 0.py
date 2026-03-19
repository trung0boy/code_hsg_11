import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

ans = 0

pos = {0:0} # lưu chỉ số xuất hiện đầu tiên của tổng thoả mãn.
curr = 0
for i in range(n):
    if A[i] > 0:
        curr += 1
    else:
        curr += -1
    if curr in pos:
        ans = max(ans, i - pos[curr] + 1)
    else:
        pos[curr] = pos.get(curr,0) + 1
print(ans)
































