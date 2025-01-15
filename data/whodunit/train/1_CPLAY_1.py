while True:
    try:
        n=input()
    except:
        exit()
    if n.count('1')==20 or n.count('0')==20:
       print("TIE")
    else:
        gc=0
        go=0
        c=0
        a=False
        b=True
        fnal=0
        for i in range(20):
            if c<10:    
                c+=1
                if i%2==0:
                    if n[i]=='1':
                        gc+=1
                else:
                    if n[i]=='1':
                        go+=1
                if i%2==0:
                    if gc>go:
                        if (go+(10-c)//2+1)<gc:
                            a=True
                            fnal=c
                            break
                    else:
                        if (gc+(10-c)//2)<go:
                            fnal=c
                            break
                else:
                    if gc>go:
                        if (go+(10-c)//2)<gc:
                            a=True
                            fnal=c
                            break
                    else:
                        if (gc+(10-c)//2)<go:
                            fnal=c
                            break
            else:
                c+=1
                if i%2==0:
                    if n[i]=='1':
                        gc+=1
                else:
                    if n[i]=='1':
                        go+=1
                if c%2==0:
                    if gc>go:
                        fnal=c
                        a=True
                        break
                    elif go>gc:
                        fnal=c
                        break
        
        if c!=20:
            if a:
                print("TEAM-A",+fnal)
            else:
                print("TEAM-B",+fnal)
        elif c==20:
            if gc==go:
                print('TIE')
            elif gc>go:
                print("TEAM-A",+fnal)
            else:
                print("TEAM-B",+fnal)
            
                
                
                    
                
            