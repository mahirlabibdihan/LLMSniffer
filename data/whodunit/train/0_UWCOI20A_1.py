T = int(input())
for _ in range(T):
    N = int(input())
    max_height = 0
    for _ in range(N):
        height = int(input())
        if height > max_height:
            max_height = height
    print(max_height)