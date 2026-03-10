import sys
sys.stdin = open('VOI 26 Bài 3 - bài đăng.INP','r')
input = sys.stdin.readline

N,Q = map(int,sys.stdin.readline().split())
A=[0]+list(map(int,sys.stdin.readline().split()))

for _ in range(Q):
    u,v = map(int,sys.stdin.readline().split())
    
    for L in range(u,v+!):
        for R in range
