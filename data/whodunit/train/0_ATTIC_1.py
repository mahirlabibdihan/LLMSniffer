def count_days(P):
    max_jump = 0
    current_jump = 0
    for i in P:
        if i == '.':
            current_jump += 1
            if current_jump > max_jump:
                max_jump = current_jump
        else:
            current_jump = 0
    return max_jump

T = int(input().strip())
for _ in range(T):
    P = input().strip()
    print(count_days(P))