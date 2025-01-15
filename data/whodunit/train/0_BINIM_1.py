def winner(T, test_cases):
    for _ in range(T):
        N, S, stacks = test_cases[_]
        if S == 'Dee' and '0' in [stack[0] for stack in stacks]:
            print('Dum')
        else:
            print('Dee')

T = int(input().strip())
test_cases = []
for _ in range(T):
    N, S = input().strip().split()
    N = int(N)
    stacks = [input().strip() for _ in range(N)]
    test_cases.append((N, S, stacks))
winner(T, test_cases)