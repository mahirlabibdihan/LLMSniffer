def min_cost(n, arr, x):
    arr.sort()
    cost = 0
    for i in range(n):
        if arr[i] < 0:
            cost += min(-arr[i], x)
    return cost

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
print(min_cost(n, arr, x))