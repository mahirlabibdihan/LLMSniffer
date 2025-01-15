T = int(input())
for _ in range(T):
    X = input()
    Y = input()
    Z = ''
    for i in range(len(X)):
        if X[i] == Y[i]:
            if X[i] == 'B':
                Z += 'W'
            else:
                Z += 'B'
        else:
            Z += 'B'
    print(Z)