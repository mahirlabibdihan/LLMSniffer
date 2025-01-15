from bisect import bisect_right

def min_moves(n, sequence):
    stack = []
    for num in sequence:
        pos = bisect_right(stack, num)
        if pos == len(stack):
            stack.append(num)
        else:
            stack[pos] = num
    return len(stack)

n = int(input().strip())
sequence = list(map(int, input().strip().split()))
print(min_moves(n, sequence))