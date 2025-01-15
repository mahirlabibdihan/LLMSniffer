for _ in range(int(input())):
    n,m = map(int,input().split())
    L = list(map(int,input().split()))
    count = 0
    for i in range(len(L)):
        if L[i] % m == 0:
            count += 1
    print(2**count-1)