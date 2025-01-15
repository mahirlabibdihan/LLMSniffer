def min_moves(n, sequence):
    stack = []
    for num in sequence:
        if not stack or stack[-1] <= num:
            stack.append(num)
        else:
            low = 0
            high = len(stack) - 1
            while low < high:
                mid = (low + high) // 2
                if stack[mid] <= num:
                    low = mid + 1
                else:
                    high = mid
            stack[high] = num
    return len(stack)

n = int(input().strip())
sequence = list(map(int, input().strip().split()))
print(min_moves(n, sequence))