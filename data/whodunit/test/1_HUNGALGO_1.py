
from sys import stdin, stdout
from collections import Counter


def solve():
    for _ in range(int(input())):
        n = int(input())
        r = [False]*(n)
        c = [False]*(n)
        for i in range(n):
            a = list(map(int, input().split()))
            for j in range(n):
                if a[j] == 0:
                    r[i] = True
                    c[j] = True

        flag = True
        for i in range(n):
            if r[i] != True or c[i] != True:
                flag = False
                break

        if flag:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
