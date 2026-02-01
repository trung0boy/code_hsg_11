def quicksort(A): # sắp xếp nhanh 
    if len(A) <=1:
        return A
    else:
        k=A[len(A)//2]
        L = [i for i in A if i < k]
        G = [i for i in A if i == k]
        R = [i for i in A if i > k]
        return  quicksort(L) + G + quicksort(R)



#chặt gỗ

def check_go(mid,A,m):
    all=0
    for h in A:
        if h>mid:
            all+= (h-mid)
    return all>=m
            
def chat_go():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    L = 0
    R=max(A)

    while L<=R:
        mid = (L+R)//2
        if check_go(mid,A,m):
            ans=mid
            L = mid+1
        else:
            R =mid-1
    print(ans)




# chạm phát sóng
def check_tram(mid,A,c):
    p=A[0]
    count=1
    for i in range(1,len(A)):
        if A[i] - p >= mid:
            count+=1
            if count >= c:
                return True
    return False

def cham_phat_song():
    n, c = map(int, input().split())
    A = list(map(int, input().split()))

    L,R = 0, A[-1]-A[0]
    ans = 0
    while L<=R:
        mid = (L+R)//2
        if check_tram(mid,A,c):
            ans = mid
            L = mid+1
        else:
            R = mid -1
    print (ans)
    
            
    





    
            
#10 3
#1 2 5 7 8 12 15 24 36 46

pos = [1, 2, 8, 12, 17]
n = len(pos)
k = 3






