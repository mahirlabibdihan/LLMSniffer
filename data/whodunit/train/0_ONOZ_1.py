T = int(input())
for _ in range(T):
    H, M = map(int, input().split())
    count = 0
    for h in range(H):
        for m in range(M):
            if h < 10 and m < 10 and h == m:
                count += 1
            elif h >= 10 and m >= 10 and h // 10 == h % 10 == m // 10 == m % 10:
                count += 1
            elif h < 10 and m >= 10 and h == m // 10 == m % 10:
                count += 1
            elif h >= 10 and m < 10 and h // 10 == h % 10 == m:
                count += 1
    print(count)