import sys

n = sys.stdin.readline()

count1 = n.count("0")
count0 = n.count("1")

print(len(n) - (count1+count0) - 1)
