for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    freq={a.count(i):i for i in set(a)}
    if len(freq)==len(set(a)):
        freq={i:a.count(i) for i in set(a)}
        current_value=a[0]
        count=1
        flag=True
        for i in a[1:]:
            if i==current_value:
                count+=1
            elif count!=freq[current_value]:
                flag=False
                break
            else:
                count=1
                current_value=i
                
        if flag:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
        
    
    