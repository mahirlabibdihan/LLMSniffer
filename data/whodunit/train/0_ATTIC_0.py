T = int(input().strip())
for _ in range(T):
    P = input().strip()
    max_jump = 0
    current_jump = 0
    for i in P:
        if i == '.':
            current_jump += 1
            if current_jump > max_jump:
                max_jump = current_jump
        else:
            current_jump = 0
    print(max_jump)