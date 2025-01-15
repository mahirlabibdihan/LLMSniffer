for t in range(int(input())):
    n=int(input())
    temp=250000
    tax=0
    p=0.00
    while p<0.30 and n-temp>=0:
        tax+=250000*p
        temp+=250000
        p+=0.05
    tax+=(n-temp+250000)*p
    print(int(n-tax))
        