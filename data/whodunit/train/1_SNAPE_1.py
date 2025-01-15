import math
t = int(input())
for t1 in range(t):
    a, b = input().split()
    a , b = int(a) , int(b)
    print(math.sqrt(b*b - a*a), math.sqrt(b*b + a*a))