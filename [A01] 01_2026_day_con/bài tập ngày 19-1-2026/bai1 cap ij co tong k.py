from collections import Counter
import sys
input = sys.stdin.readline
n,s = 6,3
A =[1,3,1,2,2]
count = 0 # dem
Ac = Counter(A)

for i in Ac:
    #print(Ac)
    
    if i+i == s and Ac[i] >= 2:
        count += (Ac[i]*(Ac[i]-1))//2
    elif s-i in Ac:
        count += Ac[i]*Ac[s-i] #ai+aj=s => s-ai = aj
        Ac[i]=0
        Ac[s-i]=0
        #print(Ac)

        
print(count)
