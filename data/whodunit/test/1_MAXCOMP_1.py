for _ in range(int(input())):
    N=int(input())
    events=[]
    for i in range(N):
        s,e,c=map(int,input().split())
        events.append([s,e,c])
    
    events.sort()
    plan=[0]*49
    for i in events:
        check_before=i[0]
        for j in range(check_before,-1,-1):
            plan[i[1]]=max(plan[i[1]] ,plan[j] + i[2])

    print(max(plan))