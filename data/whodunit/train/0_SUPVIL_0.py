T = int(input())
for _ in range(T):
    N = int(input())
    superheroes = 0
    villains = 0
    for _ in range(N):
        name = input()
        if name.endswith('man') or name.endswith('woman'):
            superheroes += 1
        else:
            villains += 1
        if superheroes - villains == 2:
            print('superheroes')
            break
        elif villains - superheroes == 3:
            print('villains')
            break
    else:
        print('draw')