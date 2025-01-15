T = int(input().strip())
for _ in range(T):
    N, S = input().strip().split()
    N = int(N)
    stacks = [input().strip() for _ in range(N)]
    if S == 'Dee' and '0' in [stack[0] for stack in stacks]:
        print('Dum')
    else:
        print('Dee')