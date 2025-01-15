import sys
import math

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        sys.stdout.write(str(math.log10(N+1)) + '\n')

if __name__ == "__main__":
    solve()