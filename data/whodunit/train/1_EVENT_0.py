a=int(input())
for t in range(a):
   s,e,l,r=input().split()
   l,r=[int(j) for j in (l,r)]
   days=["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
   x=days.index(s)
   y=days.index(e)
   if y>=x:
     diff=y-x+1
   else:
     diff=7-(x-y)+1
   adiff=(r-diff)//7-(l-diff)//7
   c=0
   val=-1
   for k in range(l-diff,r-diff+1):
       if k%7==0:
          c+=1
          val=k+diff
   if c==0:
      print("impossible")
   elif c==1:
      print(val)
   else:
      print("many")