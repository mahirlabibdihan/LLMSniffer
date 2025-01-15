import math
def overlucky(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if any(x in str(i) for x in '47'):
                count += 1
            if n//i != i:
                if any(x in str(n//i) for x in '47'):
                    count += 1
    return count

T = int(input())
for _ in range(T):
    n = int(input())
    print(overlucky(n))