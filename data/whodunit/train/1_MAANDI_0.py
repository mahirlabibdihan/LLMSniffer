from math import sqrt

def div(n):
    count = 0
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            j = n/i
            if '4' in str(i) or '7' in str(i):
                count += 1
            if '4' in str(j) or '7' in str(j):
                count += 1-(j==i)
    return count

t = int(input())
while t:
    n = int(input())
    print(div(n))
    t -= 1
    
