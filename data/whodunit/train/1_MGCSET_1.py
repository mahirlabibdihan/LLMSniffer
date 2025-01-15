test=int(input())
for t in range(test) :
  n,m =[int(x) for x in input().split()]
  a =[int(x) for x in input().split()]
  count=0
  for i in a :
      if i % m ==0 :
        count=count+1
  print(2**count-1)