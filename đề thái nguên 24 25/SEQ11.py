
n=8

A = [-1,-2,3,4,-5,1,2,3]

max_leght = 1
curr_leght = 1

max_sum= A[0]
curr_sum = A[0]


for r in range(0,n):
    if A[r] > A[r-1]:
        curr_leght +=1
        curr_sum +=A[r]
    else:
        curr_leght = 1
        curr_sum = A[r]
        
    if curr_leght > max_leght:
        max_leght = curr_leght
        max_sum =curr_sum
            
    if max_leght == max_leght:
            max_sum = max(max_sum,curr_sum)
    print(max_leght,max_sum)

        

