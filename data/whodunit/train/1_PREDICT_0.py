def solve(x, a):
    gain = 2*(1-x)*a
    return gain*x-a*(1-x)

for _ in range(int(input())):
    p = float(input())
    print(10000+solve(max(p, 1-p), 10000))