
t = int(input())

for i in range(t):
    n = list(map(int, input().split()))
    f = True
    n.sort()
    while n[1] % n[0] != 0 and n[1] // n[0] < 2:
        n[1] = n[1] % n[0]
        f = not f
        n.sort()
    print('Rich' if f == False else 'Ari')