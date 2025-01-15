t=int(input())
for i in range(t):
    n,k,m=list(map(int,input().split()))
    plan=list(map(int,input().split()))
    comp=list(map(int,input().split()))
    white=list(map(int,input().split()))
    black=list(map(int,input().split()))
    rem=[]
    p=0
    machine=[]
    count_rem=0
    count_machine=0
    for j in range(n):
        rem.append(plan[j]-comp[j])
    count_rem+=sum(rem)
    rem.sort(reverse=True)
    machine.extend(white)
    machine.extend(black)
    machine.sort(reverse=True)
    count_machine+=sum(machine)

    if machine[0]<=rem[-1]:
        count_rem-=count_machine
    elif machine[-1]>rem[0]:
        pass
    else:
        for j,val in enumerate(machine):
            while rem!=[]:
                if val<=rem[p]:
                    count_rem-=val
                    rem.pop(p)
                    break
                else:
                    break

    print(count_rem)
                 