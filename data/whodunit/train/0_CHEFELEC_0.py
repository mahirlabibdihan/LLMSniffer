T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    x = list(map(int, input().split()))
    elec = [i for i in range(n) if s[i] == '1']
    min_wire = sum(min(abs(x[i]-x[j]) for j in elec) for i in range(n) if s[i] == '0')
    print(min_wire)