for _ in range(int(input())):
     N,H,Y1,Y2,L=map(int,input().split())
     k=0
     for i in range(N):
         t,x=map(int,input().split())
         if t==2:
             if Y2>=x and L>0:
                 k+=1
             elif(Y2<x and L>=1):
                 if L==1:
                     L-=1
                 else:
                     k+=1
                     L-=1
         elif t==1:
             if H-Y1<=x and L>0:
                 k=k+1
             elif H-Y1>x and L>=1:
                 if L==1:
                     L-=1
                 else:     
                     k+=1
                     L-=1
     print(k)    
                 
                        
