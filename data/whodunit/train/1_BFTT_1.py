t = int(input())
for i in range(t):
    n = int(input())+1
    while True:
        if str(n).count("3") >= 3:
            break
        n = n+1
    print(n)