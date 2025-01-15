
for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    l = list(map(int, input().split()))
    d = []
    for i in l:
        d.append(abs(i-b) + c + abs(i-a))
    print(min(d))
    
    
    