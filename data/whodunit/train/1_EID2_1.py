t= int(input())
for _ in range(t):
    a1,a2,a3,c1,c2,c3= map(int,input().split())
    count=3
    if((a1>a2 and c1>c2) or (a2>a1 and c2>c1) or (a2==a1 and c2==c1)):
        count-=1
    if((a2>a3 and c2>c3) or (a3>a2 and c3>c2) or (a3==a2 and c3==c2)):
        count-=1
    if((a1>a3 and c1>c3) or (a3>a1 and c3>c1) or (a3==a1 and c3==c1)):
        count-=1
        
    if count==0 :
        print("FAIR")
    else:
        print("NOT FAIR")