import sys
sys.stdin = open('ptit047.txt','r')
input = sys.stdin.readline



def dev_uoc(x):
    ans = 0
    i = 1
    while i*i <= x:
        if x%i == 0:
            ans += i
            if i != x//i:
                ans += x//i
        i+=1
    return ans
                




n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

p = 0
val = None
for j in range(n):
    ui = 0
    vi = 0
    
    for i in A[:j]:
        if i > A[j]:
            ui += 1
    for k in A[j+1:]:
        if k < A[j]:
            vi += 1
            
    if ui*vi > 0:
        pi = dev_uoc(A[j]) 
        if pi > p:
            p = pi
            val = A[j]
        
if p == 0:
    print("Neu khong co Thuong, Tai se buon biet may :(")
else:
    print(pi, val)
