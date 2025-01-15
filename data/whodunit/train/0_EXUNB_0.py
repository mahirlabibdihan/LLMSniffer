T = int(input())
for _ in range(T):
    N = int(input())
    if N % 2 == 0:
        print("NO")
    else:
        print("YES")
        for i in range(N):
            for j in range(N):
                if i == j:
                    print(0, end='')
                elif (i - j + N) % N <= N // 2:
                    print(1, end='')
                else:
                    print(0, end='')
            print()