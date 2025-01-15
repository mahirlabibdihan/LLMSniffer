def num_decks(n):
    if n <= 2:
        return n    
    
    fib1, fib2 = 1, 1
    i = 1
    while fib2 < n: 
        fib1, fib2 = fib2, fib2 + fib1
        i += 1
    return i - (fib2 != n)


for _ in range(int(input())):
    n = int(input())
    
    print(num_decks(n))
    