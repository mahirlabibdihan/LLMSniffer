T=int(input())
for i in range(T):
        n=int(input())
        l=list(map(int,input().split()))
        s=dict()
        for e in l:
                if(e in s):
                        s[e]=s[e]+1
                else:
                        s[e]=1
        l1=s.values()
        print(n-max(l1))
        

