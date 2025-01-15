for _ in range(int(input())):
    s=input()
    n=len(s)
    if n==1:
        print("NO")
        continue
    if n%2==0:
        if s[:n//2]==s[n//2:]:
            print("YES")
        else:
            print("NO")
    else:
        a=s[:n//2]
        b=s[n//2:]
        f=0
        mis=0
        fa=True
        for i in range(len(a)):
            if a[i]==b[i+f]:
                continue
            elif mis==0:
                if a[i]==b[i+f+1]:
                    f+=1 
                    mis=1 
                else:
                    fa=False
                    break
            else:
                fa=False
                break
        
        if fa==True:
            print("YES")
            continue
        b=s[:n//2+1]
        a=s[n//2+1:]
        f=0
        mis=0
        fa=True
        for i in range(len(a)):
            if a[i]==b[i+f]:
                continue
            elif mis==0:
                if a[i]==b[i+f+1]:
                    f+=1 
                    mis=1 
                else:
                    fa=False
                    break
            else:
                fa=False
                break
        
        if fa==True:
            print("YES")
        else:
            print("NO")
        
        