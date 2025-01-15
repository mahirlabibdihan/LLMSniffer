def min_cost(n, arr, x):
    cost = sum([min(-i, x) for i in arr if i < 0])
    return cost

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(min_cost(n, arr, x))