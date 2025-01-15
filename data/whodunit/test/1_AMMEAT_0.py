t=int(input())
for _ in range(t):
  n,m=map(int,input().split())
  p=list(map(int,input().split()))
  if sum(p)<m:
    print(-1)
  else:
    p.sort(reverse=True)
    count=0
    res=0
    for i in p:
      count+=i
      res+=1
      if count>=m:
        print(res)
        break
        