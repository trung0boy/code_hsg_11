import heapq
import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

min1 = heapq.heappop(A)

