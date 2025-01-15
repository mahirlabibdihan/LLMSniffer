def curr_m(P,Q):
    return P+Q*2
for _ in range(int(input())):
    N,P,Q=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    count=0
    for i in range(N):
        p,q,r=P,Q,a[i]
        if curr_m(P,Q)>=a[i]:
            if a[i]%2==0:
                req_2=int(r/2)
                r-=min(q,req_2)*2
                q-=min(q,req_2)
                #print('q r',q,r)
                if r!=0:
                    req_1=r
                    r-=min(p,req_1)
                    p-=min(p,req_1)
                    #print('p r',p,r)
                if r==0:
                    count+=1
                    P,Q=p,q
            else:
                req_2=int(r/2)
                r-=min(q,req_2)*2
                q-=min(q,req_2)
                req_1=r
                r-=min(p,req_1)
                p-=min(p,req_1)
                if r==0:
                    count+=1
                    P,Q=p,q
            #print(P,Q)
    print(count)