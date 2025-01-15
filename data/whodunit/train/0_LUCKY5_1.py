def count_operations(T, numbers):
    results = []
    for i in range(T):
        N = numbers[i]
        results.append(N.count('4') + N.count('7'))
    return results

T = int(input())
numbers = []
for _ in range(T):
    numbers.append(input())
results = count_operations(T, numbers)
for result in results:
    print(result)