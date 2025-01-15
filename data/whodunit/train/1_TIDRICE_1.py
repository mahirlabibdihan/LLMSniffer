try:
    for _ in range(int(input())):
        d = {}
        for _ in range(int(input())):
            string = input().split()
            if string[1] == '+':
                d[string[0]] = 1
            else:
                d[string[0]] = -1
        print(sum(d.values()))
except EOFError:
    pass