T = int(input())
for _ in range(T):
    N, S = input().split()
    N = int(N)
    stacks = [input() for _ in range(N)]
    while True:
        if S == 'Dee':
            for i in range(N):
                if stacks[i][0] == '0':
                    stacks[i] = stacks[i][1:]
                    S = 'Dum'
                    break
            else:
                print('Dum')
                break
        else:
            for i in range(N):
                if stacks[i][0] == '1':
                    stacks[i] = stacks[i][1:]
                    S = 'Dee'
                    break
            else:
                print('Dee')
                break