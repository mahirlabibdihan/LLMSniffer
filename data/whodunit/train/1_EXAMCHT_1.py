from math import sqrt

def solve():
    a, b = map(int, input().split())
    if a == b: return -1
    t = max(a, b) - min(a, b)
    res = 0
    for i in range(1, int(sqrt(t) + 1)):
        if not t % i: res += 1 + (i != (t // i))
    return res
    

def main():
    T = int(input())
    for _ in range(T):
        print(solve())

main()