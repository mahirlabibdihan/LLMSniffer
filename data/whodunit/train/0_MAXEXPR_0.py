from sys import stdin, stdout
from math import sqrt

def solve():
    n = int(stdin.readline())
    k = list(map(float, stdin.readline().split()))
    c = list(map(float, stdin.readline().split()))
    sum_k = sum(k)
    sum_c = sum(c)
    if sum_c < 0:
        stdout.write("-1\n")
        return
    x = [c[i] - k[i] * sum_c / sum_k for i in range(n)]
    if min(x) < 0:
        stdout.write("-1\n")
        return
    stdout.write("{:.2f} ".format(sum(sqrt(xi + ci) for xi, ci in zip(x, c))))
    stdout.write(" ".join("{:.2f}".format(xi) for xi in x))
    stdout.write("\n")

t = int(stdin.readline())
for _ in range(t):
    solve()