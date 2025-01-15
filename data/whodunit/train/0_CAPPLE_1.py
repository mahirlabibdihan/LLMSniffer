T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    apples = [int(x) for x in input().strip().split()]
    print(len(set(apples)))