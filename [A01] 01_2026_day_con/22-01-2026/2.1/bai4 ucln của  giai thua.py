import math

# factorial một hàm mạnh để tính giai thừa của thư viện math
n,m = map(int,input().split())
print(math.gcd(math.factorial(n),math.factorial(n)))
