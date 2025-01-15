t=int(input())
for q in range(t):
  n,m=map(int,input().split())
  l=[0]*(m+1)
  for i in range(n):
    d,v=map(int,input().split())
    if l[d]<v:
        l[d]=v
  l.sort(reverse=True)
  print(l[0]+l[1])
        
    
        
    
  