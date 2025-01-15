def precompute():
    n=100000
    d={0:1}
    s4=[0]
    s7=[0]
    
    for i in range(1,n+1):
        v=str(i)
        s4.append(s4[-1]+v.count('4'))
        s7.append(s7[-1]+v.count('7'))
    s4_7=[0]
    for i in range(1,n+1):
        s4_7.append(s4[i]-s7[i])
    
    ans=[0]
    for i in range(1,n+1):
        v=s4_7[i]
        if v in d:
            ans.append(ans[-1]+d[v])
            d[v]+=1
        else:
            ans.append(ans[-1])
            d[v]=1
    return ans
    
ans=precompute()
for _ in range(int(input())):
    print(ans[int(input())])
    