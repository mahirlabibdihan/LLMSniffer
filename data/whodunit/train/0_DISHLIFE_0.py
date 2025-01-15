T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    ingredients = [0]*K
    for _ in range(N):
        P = list(map(int, input().strip().split()))
        for i in range(1, P[0]+1):
            ingredients[P[i]-1] += 1
    if 0 in ingredients:
        print("sad")
    elif max(ingredients) > 1:
        print("some")
    else:
        print("all")