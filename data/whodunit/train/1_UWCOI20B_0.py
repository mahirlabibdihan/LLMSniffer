for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    odd_count = 0
    even_count = 0

    for num in A:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    res = even_count * odd_count
    print(res)
