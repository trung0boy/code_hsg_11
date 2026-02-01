#Lập lịch công việc
# chọn nhiều công việc nhất có thể
# xắp xếp key=e và kiểm tra điều kiện nếu thời gian bắt đầu của công việc mới >= time kết thúc công việc trước
def lap_cong_viec():
    n = int(input())
    A=[]
    for i in range(n):
        s,e =map(int,input().split())
        A.append((s,e))
    A.sort(key=lambda x:x[1])

    count = 0
    Et =-1
    for s , e in A:
        if s >= Et:
            count+=1
            Et = e
            print(s,e)
    print(count)

import heapq

# nối dây
#Đề bài: Có N sợi dây với độ dài khác nhau.
#Mỗi bước ta chọn 2 sợi dây để nối lại với nhau, chi phí nối bằng tổng độ dài 2 sợi đó.
#Tìm tổng chi phí nhỏ nhất để nối hết N sợi dây.
#Thuật toán: Luôn chọn hai sợi dây ngắn nhất hiện có để nối.
#Công cụ: Sử dụng Priority Queue (Min-Heap) để lấy ra phần tử nhỏ nhất trong O(logN).

import heapq

def noi_day():
    n = int(input())
    A = list(map(int,input().split()))
    heapq.heapify(A)
    count = 0
    while len(A)> 1:
        first =heapq.heappop(A)
        secound = heapq.heappop(A)
        arr = first + secound
        count+=arr

        heapq.heappush(A,arr)
    print(count)
        
