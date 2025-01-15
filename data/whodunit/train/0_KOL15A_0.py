T = int(input())
for _ in range(T):
    S = input()
    print(sum(int(c) for c in S if c.isdigit()))