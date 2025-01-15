import sys
import math

def solve():
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        print(math.log10(N+1))

if __name__ == "__main__":
    solve()