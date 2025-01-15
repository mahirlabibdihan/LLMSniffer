T=int(input())
for i in range(T):
    N=int(input())
    s=input()
    x=0
    y=0
    last="Z"
    for i in range(N):
        if s[i]=="L" and last!="L" and last!="R":
            x-=1
            last="L"
        elif s[i]=="R" and last!="R" and last!="L":
            x+=1
            last="R"
        elif s[i]=="U" and last!="U" and last!="D":
            y+=1
            last="U"
        elif s[i]=="D" and last!="D" and last!="U":
            y-=1
            last="D"
    print(x,y)
            