t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    f = [0]*2001
    for i in a:
        f[i]+=1

    ans1,ans2 = 0,0
    for i in range(-1000,1001,1):
        if f[i]!=0:
            for j in range(i,1001,2):
                if f[j]!=0:
                    if i==j:
                        # print(f[i])
                        ans1+=((f[i]*(f[i]-1))//2)
                    elif (i+j)%2==0 and f[(i+j)//2] != 0:
                        ans2+= (f[i]*f[j])

    print(ans1+ans2)