for _ in range(int(input())):
   a, b, c = map(float, input().split())
   ans = 0
   tam = a * b
   for i in range(int(c)):
      x, y, z = map(float, input().split())
      if tam > z / x + b * y:
         ans = i + 1
         tam = z / x + b * y
   print(ans)
         