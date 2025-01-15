T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    apples = list(map(int, input().strip().split()))
    unique_apples = set(apples)
    print(len(unique_apples))