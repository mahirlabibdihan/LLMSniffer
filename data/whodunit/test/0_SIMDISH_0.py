T = int(input())
for _ in range(T):
    dish1 = set(input().split())
    dish2 = set(input().split())
    if len(dish1.intersection(dish2)) >= 2:
        print("similar")
    else:
        print("dissimilar")