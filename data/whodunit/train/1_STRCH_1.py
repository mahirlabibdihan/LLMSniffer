op=[]
def sumn(n): 
    return (n*(n+1))//2

t=int(input())
while t>0:
    n=int(input())
    mainsum=sumn(n)
    inpt=[str(x) for x in input().split()]
    miss=inpt[0].split(inpt[1])
    summiss=0
    for i in range(0,len(miss)):
        summiss+=sumn(len(miss[i]))
    
    print(mainsum-summiss)
    t-=1