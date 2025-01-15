try:
    t=int(input())
    for i in range(t):
        a,b=map(int,input().split())
        i=10
        temp=0
        tot=a+b
        while(a or b):
            if(a%10)+(b%10)>9:
                temp+=i
            a=a//10
            b=b//10
            i=i*10
        print(tot-temp)    
except:
    EOFError