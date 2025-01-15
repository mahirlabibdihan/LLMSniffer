for _ in range(int(input())):
    n=int(input())
    if n==0:
        print('Draw')
        continue
    teamA=input()
    teamB=''
    a=1
    b=0
    for i in range(n-1): 
        s=input()
        if s==teamA:
            a=a+1 
        else:
            teamB=s 
            b=b+1 
    if a==b:
        print('Draw')
    elif a>b:
        print(teamA)
    elif a<b:
        print(teamB)
        