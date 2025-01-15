for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = a.count(1)
    pairs = 0
    for i in range(len(a)):
        for j in range(i + 1 , len(a)):
            if a[i] & a[j] == a[i]:
                pairs = pairs + 1
    print(pairs)