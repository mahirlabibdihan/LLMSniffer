a = [1]
from random import *

for t in range(int(input())):
    n = int(input())
    i = 1
    while i * i < n:
        i += 1
    x = ["X"] * i
    d = ["D"] * i

    w = i * i - n
    if w <= i:
        x = x[:i - w] + ["D"] + x[i - w:]
        d.pop()
    elif 2 * i > w > i:
        d.pop()
        x.pop()
        w -= i
        d = d[:w] + ["X"] + d[w:]
    ans="".join(x + d)
    if ans[0]=="D":
        ans=ans[1:]
    print(ans)