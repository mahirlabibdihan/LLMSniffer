for _ in range(int(input())):
  n=int(input())
  li=[int(x) for x in input().split()]
  m=max(li)
  print(n-m)