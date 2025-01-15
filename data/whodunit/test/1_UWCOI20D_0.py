t=int(input())
for _ in range(t):
    n=int(input())
    if(n==1):
        m=int(input())
        print(1)
    else:
        m=[]
        indexes=[]
        for i in range(n):
            l=input()
            temp=l.index('1')
            indexes.append(temp)
            m.append(l)
        
        counter=0
        for i in range(n):
            left=indexes[i]
            right=indexes[i]
            for j in range(i,n):
                left=min(indexes[j],left)
                right=max(indexes[j],right)
                if(right-left == j-i):
                    counter+=1
        print(counter)

            
    