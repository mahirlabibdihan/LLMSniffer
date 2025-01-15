N = int(input())
recipes = {}
for _ in range(N):
    recipe, priority = input().split()
    priority = int(priority)
    if recipe in recipes:
        recipes[recipe] = max(recipes[recipe], priority)
    else:
        recipes[recipe] = priority

Q = int(input())
for _ in range(Q):
    query = input()
    matching_recipes = [recipe for recipe in recipes if recipe.startswith(query)]
    if matching_recipes:
        print(max(matching_recipes, key=recipes.get))
    else:
        print("NO")