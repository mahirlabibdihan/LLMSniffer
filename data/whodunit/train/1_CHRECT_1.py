from math import ceil
t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    if n == 1 or m == 1:
      if n <= 2 and m <= 2:
          print(0)
      else:
          print(k)
    elif n > 1 and m > 1:
        if k <= 2:
          print(1)
        else:
          print(ceil(k / 2)) 