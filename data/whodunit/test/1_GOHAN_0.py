t = int(input())
for _ in range(t):
  r, l, c, lol = [float(a) for a in input().split()]
  R = r
  C = c
  L = l
  val = -(R)/(2*L)
  ans = val * val * L * C + 1 + R * val * c
  print(ans) 