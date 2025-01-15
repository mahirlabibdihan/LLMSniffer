T = int(input())
for t in range(T):
    S,E,L,R = input().split()
    L,R = [int(i) for i in (L,R)]
    
    
    days= ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday" ,"friday"]
    S_ind = days.index(S)
    E_ind = days.index(E)
    
    if E_ind >= S_ind:
        diff = E_ind - S_ind + 1
    else:
        diff = 7 - (S_ind-E_ind) + 1
        
    ans_diff  = (R-diff)//7 - (L-diff)//7
    

    count = 0
    last_val = -1
    for i in range(L-diff,R-diff+1):
        if i%7== 0:
            count +=1
            last_val = i+diff
    if count == 0:
        print('impossible')
    elif count == 1:
        print(last_val)
    else:
        print('many')
             