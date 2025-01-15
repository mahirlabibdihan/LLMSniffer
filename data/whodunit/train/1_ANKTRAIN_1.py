def get_train_partner(n):
    res = n%8
    if res==0:
        return str(n-1)+"SL"
    elif res==7:
        return str(n+1)+"SU"
    elif res==1:
        return str(n+3)+"LB"
    elif res==4:
        return str(n-3)+"LB"
    elif res==3:
        return str(n+3)+"UB"
    elif res==6:
        return str(n-3)+"UB"
    elif res==2:
        return str(n+3)+"MB"
    else:
        return str(n-3)+"MB"

for i in range(int(input())):
    n = int(input())
    print(get_train_partner(n))