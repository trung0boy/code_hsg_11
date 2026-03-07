import sys


def tach_id(n):
    pos = {} #val : id # với mỗi số ta gán bằng 1 id
    ans = 0

    id_val = 0
    for val in str(n):
        if val not in  pos:
            id_val +=1
            pos[val] = id_val
        ans = ans*10 + (pos[val])            
    return ans




n = int(sys.stdin.readline())

count = 0
pos = {} #ans:val # id được trả về : đồng đẳng
for x in range(1,n+1):
    ans = tach_id(x)
    if ans not in pos:
        pos[ans] = x
    count += pos[ans]
print(count)
    

