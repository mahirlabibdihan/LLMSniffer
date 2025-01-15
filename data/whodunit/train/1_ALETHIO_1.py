p = input()
if(len(p)>=1 and len(p)<=1000):     
    i = 0
    k = 0
    x = 0
    m = 0
    while(i < len(p)):
        if(p[i].isdigit()):
            j = i
            c = ''
            k = 0
            if(i > 0):
                if(p[i-1].isalpha()):
                    c = c+'9'
                    k=1
                    if(i>1 and p[i-2].isdigit()):
                        c = p[i-2] + c
                if(p[i-1].isdigit() and int(p[i-1]!=0)):
                    c = c + p[i-1]
            while(i<len(p)):
                if(p[i].isdigit()):
                    c = c + p[i]
                if(p[i].isalpha()):
                    if(k==1):
                        break
                    k = 1
                    c = c + '9'
                i = i+1
            if(int(c) > x):
                x = int(c)
            i = j
        else:
            m = m+1
        i= i+1
    if(x==0 and m==len(p)):
        print(9)
    else:
        print(x)