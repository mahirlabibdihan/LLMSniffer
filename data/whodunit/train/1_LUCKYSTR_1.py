k,n=map(int,input().split())
a=[]
b=[]
for _ in range(k):
    a.append(input())
for _ in range(n):
    b.append(input())


for i in b:
    f1=0 
    f2=0
    if len(i)>=47:
        f1=1
    for j in a:
        if j in i:
            f2=1 
            break 
            
    if (f1 or f2):
        print("Good")
    else:
        print("Bad")
                
    