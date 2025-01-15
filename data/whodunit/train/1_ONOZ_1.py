def getCount(h,m,i) :
    h=int(h)
    m=int(m)
    h1=0
    lst=[11,22,33,44,55,66,77,88,99]
    while(h1<h) :
        for m1 in range(0,m) :
            if h1<10 :
                if(m1<10 and h1==m1) : count[i]+=1
                if (m1 in lst and m1%10==h1) :  count[i]+=1
            else :
                if(m1 in lst and h1==m1) : count[i]+=1
                if(h1 in lst and h1%10==m1) : count[i]+=1
        h1+=1
t=int(input())
count=[0]*t
for i in range(0,t) :
    h,m=input().split()
    getCount(h,m,i)

for i in count : print(i)
