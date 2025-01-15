def total_memory_allocated(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        memory = test_cases[_][1]
        total_memory = 0
        current_memory = 0
        for i in range(N):
            if memory[i] > current_memory:
                total_memory += memory[i] - current_memory
            current_memory = max(current_memory, memory[i])
        print(total_memory)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    memory = list(map(int, input().split()))
    test_cases.append((N, memory))
total_memory_allocated(T, test_cases)