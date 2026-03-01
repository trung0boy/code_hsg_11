import sys

n,m = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
Q =[]

for i in range(m):
    Mi = list(map(int,sys.stdin.readline().split()))
    Q.append(Mi)


for q in Q:
    if q[0] == 1: # loại 1
        print(
            sum(
                A[q[1]-1 : q[2]] # từ x -> y
                )
            )
        #print('1',A[q[1]-1 : q[2]])
        
    if q[0] == 2: # loại 2
        for i in range(q[1]-1, q[2]):
            A[i] = A[i]%q[3]
        #print('2',A)
        
    if q[0] == 3: # loại 3
        A[q[1]-1] = q[2]
        #print('3',A)


















