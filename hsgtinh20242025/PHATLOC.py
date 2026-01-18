import sys
input = sys.stdin.readline

prefix = [0]*(10**6)
for i in range(len(prefix)):
    prefix[i] = prefix[i-1]
    if '6' in str(i):
        prefix[i]+=1

        
T = int(input())       
A=[]
for i in range(T):
    l,r = map(int,input().split())
    A.append((l,r))
    
for l,r in A:
    print(prefix[r] - prefix[l-1])
    



