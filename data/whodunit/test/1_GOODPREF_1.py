t=int(input())
for i in range(t):
    a,k=map(str,input().split(" "))
    hash1=[0,0]
    k=int(k)
    ans=0
    a1=0
    b1=0
    for j in range(k):
        count=0
        for l in range(len(a)):
            if a[l]=='a':
                a1+=1
            else:
                b1+=1
            if a1>b1:
                count+=1
        if count==0:
            break
        elif count==len(a):
            ans=ans+(k-j)*count
            break
        elif a1==b1:
            ans+=(k-j)*count
            break
        else:
            ans+=count
    print(ans)