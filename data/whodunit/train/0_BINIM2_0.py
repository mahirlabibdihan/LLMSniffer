T = int(input())
for _ in range(T):
    N, S = input().split()
    N = int(N)
    stacks = [input() for _ in range(N)]
    while True:
        if S == 'Dee':
            if '0' in stacks:
                stacks.remove('0')
                S = 'Dum'
            else:
                print('Dum')
                break
        else:
            if '1' in stacks:
                stacks.remove('1')
                S = 'Dee'
            else:
                print('Dee')
                break