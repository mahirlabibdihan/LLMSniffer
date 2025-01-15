t=int(input()) 
for i in range(t):
   n1,n2,m=list(map(int,input().split())) 
   x=(m*(m+1))//2
   a=min(n1,n2) 
   b=max(n1,n2) 
   if x>a:
      x=a 
   a-=x 
   b-=x 
   print(a+b)
   
   
      
   