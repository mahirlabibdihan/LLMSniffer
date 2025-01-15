from math import *
for _ in range(int(input())):
   n,m,k = map(int,input().split())
   if n+m<=3:
      print(0)
   elif n==1 or m==1:
      print(k)
   else:
      print(ceil(k/2))

   