for i in range(int(input())):
    n,h,y1,y2,l=map(int,input().split())
    ctr=0
    for j in range(n):
        t,x=map(int,input().split())
        if t==2 and l!=0:
            if y2>=x:
                ctr+=1
            else:
                l-=1
                if l>=1:
                    ctr+=1
        elif t==1 and l!=0:
            if h-y1<=x:
                ctr+=1

            else:
                l-=1
                if l>=1:
                    ctr+=1
                
    print(ctr)
            
                
        
       

