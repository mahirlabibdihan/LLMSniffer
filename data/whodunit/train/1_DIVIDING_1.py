n=int(input())
lst=list(map(int,input().split()))
main=list(lst)
sum_stamps=0
men=0
if len(main)==n :
    for i in lst:
        sum_stamps+=i
    dig=n
    while dig>=0:
        men=men+dig
        dig=dig-1
    if men == sum_stamps :
        print("YES")
    else:
        print("NO")
            


