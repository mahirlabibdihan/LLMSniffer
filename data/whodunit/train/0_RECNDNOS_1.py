T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    types = set(A)
    max_dishes = 0
    dish_type = 0
    for t in types:
        dishes = [i for i in range(N) if A[i] == t and (i == 0 or A[i-1] != t) and (i == N-1 or A[i+1] != t)]
        if len(dishes) > max_dishes:
            max_dishes = len(dishes)
            dish_type = t
        elif len(dishes) == max_dishes:
            dish_type = min(dish_type, t)
    print(dish_type)