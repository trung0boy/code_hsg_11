import sys
sys.setrecursionlimit(10**9)

n  = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

A.sort()

print(max(
                A[n-1] * A[n-2] * A[n-3],
                A[0]   * A[1]  * A[-1],
                A[0] * A[1] * A[2] 
                 ))
