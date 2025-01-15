T = int(input())
for _ in range(T):
    H, M = map(int, input().split())
    count = 0
    for h in range(H):
        for m in range(M):
            if len(set(str(h) + str(m))) == 1:
                count += 1
    print(count)