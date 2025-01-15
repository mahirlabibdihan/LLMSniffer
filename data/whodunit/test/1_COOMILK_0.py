for _ in range(int(input())):
   n=int(input())
   a=[]
   a=list(map(str,input().split()))
   s=0
   if a[n-1]=='cookie':
       print('NO')
   else:
       for i in range(n-1):
           if a[i]=='cookie' and a[i+1]=='cookie':
               print("NO")
               s=1
               break
       if s==0:
            print('YES')
        