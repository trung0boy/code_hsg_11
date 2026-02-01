import time
import sys
import random

#= = = = = = = = = =

#dãy con tăng dài nhất:  O(N**2)

def day_tangON2():
    n = int(input())
    A = list(map(int, input().split()))
    dp = [1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j]+1)
    max_leght=max(dp)
    print(dp)
    
    # n = 7
    #A =    2 5   3 6  2  4 5
    #max_leght  = 4
    #dp = [1, 2, 2, 3, 1, 3, 4]
    # độ dài lớn nhất của dãy là phần tử lớn nhất của dp
    # phần tử thứ 2 của dãy là phần tử nhỏ hơn nó ở 1 và ở cuối cùng của dãy liên tiếp bằng nhau.
    # nếu có nhiều max thì dãy đó có bằng đó max
    # truy hồi
    while max_leght in dp: # truy hòi nhiều dãy 
        idx = dp.index(max_leght) # ta truy hồi từ chỉ số của số lớn nhất
        i = idx
        pos=[A[idx]]
        while i!=0: # truy hồi 1 dãy
            if dp[i] != dp[i-1] and dp[i-1] != -1:
                pos.append(A[i-1])
            i-=1
        print(pos)
        dp[idx] = -1

#= = = = = = = = = = = = = = = = =
        
import bisect
def day_tangONlogN():
    
    n = int(input())
    A = list(map(int, input().split()))

    tails =[]
    for x in A:
        idx = bisect.bisect_left(tails,x) # lấy chỉ số chèn left nhất của x
        if len(tails)==idx:
            tails.append(x) # mở rộng dãy
        else: # thay thế khi idx < độ dài 
            tails[idx] = x 
        print(tails)
    print(len(tails))
    print(tails)





























    
