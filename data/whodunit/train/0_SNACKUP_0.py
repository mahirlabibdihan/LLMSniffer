T = int(input())
for _ in range(T):
    n = int(input())
    print(n)
    for i in range(1, n+1):
        print(n)
        for j in range(1, n+1):
            print(j, i, (i+j-2)%n+1)