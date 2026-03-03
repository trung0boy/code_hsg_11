import sys
import random
import time

def randomA(n):
    A =[]
    for i in range(n):
        A.append(random.randint(1,101))
    return A


def hang_cay(n,A):
    if len(set(A)) == 1:
        print(A[0],n)
    else:
        minA = min(A)
        n_min = A.count(minA)
        print( minA, len(A) - n_min)

n = 1000000
A = randomA(n)
#n = int(sys.stdin.readline())
#A = list(map(int,sys.stdin.readline().split()))

hang_cay(n,A)
