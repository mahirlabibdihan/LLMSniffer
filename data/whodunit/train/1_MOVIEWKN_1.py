def movie_weekend(a, b):
    l = []
    k = []
    for i in range(1, len(a)+1):
        l.append(tuple([a[i-1], b[i-1], i]))

    mul = list(map(lambda x: x[0]*x[1], l))
    max_m = max(mul)
    for i in range(len(mul)):
        if mul[i]==max_m:
            k.append(l[i])
    if max(k, key=lambda x: x[1]) != min(k, key=lambda x: x[1]):
        return max(k, key=lambda x: x[1])[2]
    else:
        return k[0][2]

for _ in range(int(input())):
    n = input()
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    print(movie_weekend(a, b))