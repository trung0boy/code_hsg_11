import sys
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

max_A = max(A)
parent = [1]*(max_A+1)

for i in range(2,max_A+1):
    for j in range(i,max_A+1,i):
        parent[j] += i

count = 0
for x in A:
    if parent[x]  < (2*x) and x > 1:
        count +=1
        #print(parent[x],x*2,x)
print(count)

#fulll
