# tạm thời chưa được
def uoc(n):
    curr=0
    for i in range(1,n+1):
        if n%i==0:
            curr+=i
    return curr

def anti(n):
    pos={}
    leght = 0
    for i in range(1,n):
        curr = uoc(i)
        if curr in pos:
            print(pos[curr], i)
        else:
            pos[curr]=i
    return
            
# ===

n =100000

parent = [0]*(n+1)

for i in range(1,n+1):
    for j in range(i*2,n+1,i): # không kể chính nó 
        parent[j] += i

    
for a in range(1,n+1):
    b =parent[a]
    if a < b <= n and parent[b] == a:
        print(a,b)
        






























