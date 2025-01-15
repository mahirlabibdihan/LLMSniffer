import math
def overlucky(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if '4' in str(i) or '7' in str(i):
                count += 1
            if n//i != i:
                if '4' in str(n//i) or '7' in str(n//i):
                    count += 1
    return count

T = int(input())
for _ in range(T):
    n = int(input())
    print(overlucky(n))