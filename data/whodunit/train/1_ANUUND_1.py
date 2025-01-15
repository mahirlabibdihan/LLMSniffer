t = int(input())
while t>0:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if n%2==0: m = n//2
    else: m = n//2 + 1
    i, j = 0, m
    while i<m and j<n:
        print(str(arr[i]) + " " + str(arr[j]), end = " ")
        i = i+1
        j = j+1
    while i<m:
        print(str(arr[i]))
        i = i+1
    print()
    t -= 1
