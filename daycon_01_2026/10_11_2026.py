"bai 1"


import copy
a=[1,3,5,7]
b=[0,1,2,1,4,3,5]   # n =8 i=7
b2 = copy.deepcopy(b)
d=0
for i in range(len(a)):
    
    if not a[i] in  b:
        print('no1')
        break
    else:
        k = b.index(a[i])
        d+=1
        print('f',d)

    if len(b)-1-k < len(a)-(i+1):
        print('no2')
        break
    
    if len(b)-1-k == 0 and i < len(a)-1:
        print('no3')
        break
       
        print('d',k)
        
if d == len(a):
    print('y')
    
        



"""
'''
bai 2: kiem tra xem b co trong a khong 
'''

a = [0,1,2,2,1,4,3,5,7] 
b = [1,2,1] 
n=len(a)
m=len(b)
k = False
for i in range(n-m):
    if a[i:i+m] == b:
        
print(k)



"""
"""
'''
 bai 3 dem so xuat hien nhieu nhat tren 1 khoang
'''

a = [1,1,1,0,0,0,0,0,4,5,6,8,8]
n=len(a)

k =1
for i in range(n):
    for j in range(n):
        b = a[i:j]
        if len(set(b)) == 1 and len(b) > k:
            k = len(b)
print(k)
        
        

"""

"""
'''
bai 5
'''

a = [1,2,3,4,5,6,1,1,6,8]
k = min(a)

for i in range(len(a)):
    if a[i] == k:
        print(i+1,end=' ')
b = sorted(a)

"""
"""
'''
bai 7
'''

    
a = [1,1,3,2,1,3,3,3,3,2,4]
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
for i in b:
    print(i, end=' ')
"""





