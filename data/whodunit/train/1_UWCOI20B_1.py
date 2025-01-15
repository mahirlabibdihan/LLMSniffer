
#2 4 6 8 3 3

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    oddcount=0
    evencount=0
    for i in l:
        if i%2==1:oddcount+=1
        else:evencount+=1
    print(oddcount*evencount)