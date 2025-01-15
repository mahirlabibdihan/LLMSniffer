#attic cross
from sys import stdin,stdout
inp = stdin.readline

t=int(inp())

while(t):
  t-=1
  s=inp()
  e=0;d=0;k=0
  if s.count('.')==0:
      print(0)
  else:
      for i in s:
        if(i=='.'):
          e+=1
          
        else:
          if(e>d):  k+=1;d=e
          e=0
      print(k)