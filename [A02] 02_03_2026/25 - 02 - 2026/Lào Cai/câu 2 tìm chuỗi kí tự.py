def countN(A,i,nA,count):
    if A[i] == "H":
        for j in range(i+1,len(A)-1):
            if A[j] in nA:
                break
            if A[j] == "S":
                for k in range(j,len(A)):
                    if A[k] in nA:
                        break
                    if A[k] == "G":
                        count+=1
    return count



import sys
T = int(sys.stdin.readline())
A = str(sys.stdin.readline())
nA = {'A','E','I','O','U'}
count =0
count2 = 0
if T == 2:
    for i in range(len(A)-2):
        count2 += countN(A,i,nA,count)
    print(count2)


if T == 1:
    for i in range(len(A)):
        if A[i] == "H":
            for j in range(i+1,len(A)-1):
                if A[j] == "S": 
                    count += A[j::].count("G")


    print(count)
