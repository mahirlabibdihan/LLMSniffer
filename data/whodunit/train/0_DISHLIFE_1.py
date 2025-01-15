T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    ingredients = set()
    redundant = False
    for _ in range(N):
        P = list(map(int, input().strip().split()))
        island_ingredients = set(P[1:])
        if len(ingredients & island_ingredients) > 0:
            redundant = True
        ingredients.update(island_ingredients)
    if len(ingredients) < K:
        print("sad")
    elif redundant:
        print("some")
    else:
        print("all")