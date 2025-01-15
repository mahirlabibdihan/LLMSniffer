T = int(input())
for _ in range(T):
    X = input()
    Y = input()
    Z = ['B' if X[i] != Y[i] else 'W' if X[i] == 'B' else 'B' for i in range(len(X))]
    print(''.join(Z))