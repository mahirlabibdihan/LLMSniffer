for _ in range(int(input())):
    X = input()
    Y = input()
    
    Z = ''.join('W' if x == 'B' and y == 'B' else 'B' for x, y in zip(X, Y))
    print(Z)