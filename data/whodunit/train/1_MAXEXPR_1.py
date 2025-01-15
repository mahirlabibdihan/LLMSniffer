for _ in range(int(input())):
  n = int(input())
  k = list(map(float, input().split()))
  c = list(map(float, input().split()))
  p = sum(x*y for (x, y) in zip(k, c))
  if p < 0:
      print(-1)
      continue
  x = [1.0/i/i for i in k]
  q = sum(i*j for i, j in zip(x, k))
  x = [i*p/q for i in x]
  f = sum(i**0.5 for i in x)
  x = [i - j for i, j in zip(x, c)]
  print(f, *x)