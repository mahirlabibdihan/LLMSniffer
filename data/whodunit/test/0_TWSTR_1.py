N = int(input())
recipes = {}
for _ in range(N):
    recipe, priority = input().split()
    priority = int(priority)
    recipes[recipe] = priority

Q = int(input())
for _ in range(Q):
    query = input()
    matching_recipes = sorted([(recipe, priority) for recipe, priority in recipes.items() if recipe.startswith(query)], key=lambda x: x[1], reverse=True)
    if matching_recipes:
        print(matching_recipes[0][0])
    else:
        print("NO")