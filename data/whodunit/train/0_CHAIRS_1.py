T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    chairs = input().strip()
    children = [i for i in range(N) if chairs[i] == '1']
    total_children = len(children)
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + ((i - 1) in children)
    min_operations = float('inf')
    for i in range(N):
        operations = prefix_sum[i + total_children] - prefix_sum[i]
        min_operations = min(min_operations, operations)
    print(min_operations)