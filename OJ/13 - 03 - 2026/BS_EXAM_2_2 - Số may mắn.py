import sys
from collections import deque
def sinh_so(k): # 6,8,66,68,666,668,686,688,... lấy số đầu + 6 và + 8
    q =deque(['6','8'])
    for i in range(k-1):
        x = q.popleft()
        q.append(x+'6')
        q.append(x+'8')
    return q[0]
k = int(sys.stdin.readline())
print(sinh_so(k))




'''

'''
    
