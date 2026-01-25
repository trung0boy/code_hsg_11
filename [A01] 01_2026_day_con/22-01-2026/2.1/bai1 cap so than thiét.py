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
            
