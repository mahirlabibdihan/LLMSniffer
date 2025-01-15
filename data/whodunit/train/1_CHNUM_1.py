t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    negative=0
    positive=0
    for i in a:
        if i<0:
            negative+=1
        else:
            positive+=1
    if negative==0:
        print(positive,positive)
    elif positive==0:
        print(negative,negative)
    else:
        print(max(positive,negative),min(positive,negative))
            
