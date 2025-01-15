def solve(m,o,p):
    sum_m=sum(m)
    sum_o=sum(o)
    sum_p=sum(p)
    maxi=0
    for i in range(0,len(m)):
        sum_=m[i]+o[i]+p[i]
        if(sum_%2!=0 and sum_>maxi):
            maxi=sum_
        elif(sum_>maxi and sum_-1>maxi):
            if(sum_%2==0):
                maxi=sum_-1
    if(sum_m%2==0):
        sum_m-=1
    if(sum_o%2==0):
        sum_o-=1
    if(sum_p%2==0):
        sum_p-=1
    return max(maxi,sum_m,sum_o,sum_p)









n=int(input())
results=[]
for i in range(0,n):
    M=list(map(int,input().split()))
    O=list(map(int,input().split()))
    P=list(map(int,input().split()))
    out=solve(M,O,P)
    results.append(out)

for i in results:
    print(i)
