import heapq



n = int(input())
A=list(map(int,input().split()))
ans = 0



heapq.heapify(A)
while len(A) >1:
    cost1 = heapq.heappop(A) # lấy min và xoá luân khỏi danh sách
    cost2 = heapq.heappop(A) 

    count = cost1+cost2 # tổng giá trị hai dây đó
    heapq.heappush(A,count) # đưa tổng 2 sợi đó vào danh sách để tính tiếp
    ans += count
print(ans)
