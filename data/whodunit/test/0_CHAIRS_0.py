T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    chairs = input().strip()
    children = [i for i in range(N) if chairs[i] == '1']
    total_children = len(children)
    min_operations = float('inf')
    for i in range(N):
        operations = sum((children[j] - i + N) % N for j in range(total_children))
        min_operations = min(min_operations, operations)
    print(min_operations)