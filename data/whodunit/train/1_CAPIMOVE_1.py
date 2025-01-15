for _ in range(int(input())):
    n = int(input())
    populations = [0]
    populations.extend([int(i) for i in input().split()])
    d = {populations[i]: i for i in range(1, n+1)}
    ports = {}
    populations.sort(reverse=True)
    for _ in range(n-1):
        u, v = map(int, input().split())
        if u in ports.keys():
            ports[u].append(v)
        else:
            ports[u] = [v, u]
        if v in ports.keys():
            ports[v].append(u)
        else:
            ports[v] = [u, v]
    for i in range(1, n+1):
        out = 0
        s = ports[i]
        for j in populations:
            if d[j] not in s:
                out = d[j]
                break
        print(out, end=" ")
    print("")