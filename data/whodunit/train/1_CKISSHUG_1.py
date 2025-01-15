import math
for _ in range(int(input())):
    n=int(input())
    p=(pow(2,math.ceil((n+1)/2),10**(9)+7)+pow(2,math.floor((n+1)/2),10**(9)+7)-2)%(10**(9)+7)
    print(p)