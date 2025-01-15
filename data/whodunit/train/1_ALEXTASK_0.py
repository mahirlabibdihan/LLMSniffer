import math
for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    least = None
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            lcm = (arr[i]*arr[j])//math.gcd(arr[i], arr[j])
            if least == None or lcm <= least:
                least = lcm
    print(least)
