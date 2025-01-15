T = int(input())
for _ in range(T):
    dish1 = input().split()
    dish2 = input().split()
    common = [ingredient for ingredient in dish1 if ingredient in dish2]
    if len(common) >= 2:
        print("similar")
    else:
        print("dissimilar")