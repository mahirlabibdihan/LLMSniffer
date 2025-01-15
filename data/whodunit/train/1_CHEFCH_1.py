for _ in range(int(input())):
    s=list(input())
    n=len(s)
    c1=0
    c2=0
    if(n%2==0):
        s1="-+"*(n//2)
        s2="+-"*(n//2)
    else:
        s1="-+"*(n//2)
        s1+="-"
        s2="+-"*(n//2)
        s2+="+"
    s1=list(s1)
    s2=list(s2)
    for i in range(n):
        if(s[i]!=s1[i]):
            c1+=1
        if(s[i]!=s2[i]):
            c2+=1
    print(min(c1,c2))
        