import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
def solve():
    pass
    l, r = map(int, input().split())
    print(r) if r-l <= l-1 else print(-1)


for _ in range(int(input())):
    solve()
