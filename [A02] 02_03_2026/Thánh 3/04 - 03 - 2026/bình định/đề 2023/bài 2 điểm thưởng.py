import sys
sys.stdin = open('bai2.INP','r')
input = sys.stdin.readline

n_g = int(sys.stdin.readline())

for ngi in range(n_g):
    n = int(sys.stdin.readline())
    pos =[list(map(int,sys.stdin.readline().split()))]
    
    print('pos',pos)
    ans_winner = 0
    while pos:
        A = pos.pop()
        if len(A) == 1:
            break
        
        ans_left = A[1]
        ans_right = A[-2]

        #xử lí lấy min mid. có tổng lớn nhất
        idx = -1
        ans_mid = float('-inf')#tổng trung bình lớn nhất.
        idx_start = 1 # chỉ số từ vị trí min đầu tiên thấy.

        if len(A) > 2:
            min_ans_mid = min(A[idx_start:len(A)-1])
            #print(min_ans_mid)
            count_min_ans_mid = A[idx_start:len(A)-1].count(min_ans_mid)
            
        while count_min_ans_mid > 0: # trường hợp trong đoạn mid có nhiều hơn 1 min
            idx_i = A[idx_start:len(A)-1].index(min_ans_mid) # chỉ số của từng min.
            ans_mid_i = (A[idx_start+idx_i-1] + A[idx_start+idx_i +1])/2 #tính tổng trung bình tại idx_i.
            print('A.A.B',A[idx_start+idx_i-1] , A[idx_start+idx_i +1])
            if ans_mid < ans_mid_i: # lấy tổng và chỉ số tại tổng trung bình lớn hơn.
                ans_mid = ans_mid_i
                idx = idx_start + idx_i
            idx_start = idx_i+1 # cập nhật chỉ số bắt đầu để tìm đoạn đằng sau
            count_min_ans_mid -= 1
        #print(idx)
        #print('A.A.A',ans_mid)
            print('A.A.C',ans_left,ans_mid, ans_right)
            
        # lấy tổng lớn nhất
        if ans_left >= ans_right and ans_left >= ans_mid:   # >>,>=,==,=>
            #if ans_left == 
            print('A1')
            ans_winner += ans_left
            A.remove(A[0])
            pos.append(A)
            print('A1.1',A)
            
            
        elif ans_right >  ans_left   and ans_right >= ans_mid:  # >>,>=
            print('A2')
            ans_winner += ans_right
            A.pop()
            pos.append(A)
            print('A2.2',A)
            
            
        else :  #>>,>= 
            print('A3')
            #print('A3.3', ans_left,ans_mid,ans_right)
            ans_winner += ans_mid
            pos.append(A[:idx])
            pos.append(A[idx+1:])
            print('A3.1',A[:idx],A[idx+1:])
    print(ans_winner)
            
        












































    
