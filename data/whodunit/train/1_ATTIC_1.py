t=int(input())

for x in range(t):
    s=input()
    l=[]
    count=0
    for i in s:
        if i=='.':
            count+=1
        else:
            if count!=0:
                l.append(count)
            count=0
    if count!=0:
        l.append(count)
    if len(l)==0:
        print('0')
    else:
        sum=1
        max=l[0]
        for i in range(1,len(l)):
            if max<l[i]:
                sum+=1
                max=l[i]
        print(sum)

    