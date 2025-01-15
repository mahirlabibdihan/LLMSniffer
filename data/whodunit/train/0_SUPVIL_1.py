def fight_result(names):
    superheroes = sum(1 for name in names if name.endswith('man') or name.endswith('woman'))
    villains = len(names) - superheroes
    if superheroes - villains == 2:
        return 'superheroes'
    elif villains - superheroes == 3:
        return 'villains'
    else:
        return 'draw'

T = int(input())
for _ in range(T):
    N = int(input())
    names = [input() for _ in range(N)]
    print(fight_result(names))