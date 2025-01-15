def is_ciel(n):
    n3 = 0
    n5 = 0
    n8 = 0
    
    while n>0:
        k = n%10
        if(k==3):
            n3+=1
        elif(k==5):
            n5+=1
        elif(k==8):
            n8+=1
        else:
            return 0
        n //= 10
  
    if(n3 <= n5 and n5 <= n8):
        return 1
    return 0

if __name__ == "__main__":
    res=0
    for _ in range(int(input())):
        buf=input()
        length=len(buf)
        st=-1
        for i in range(length-1,-1,-1):
            if(buf[i]==' '):
                st=i
                break
    
        p=int(buf[i+1:length])
        if(is_ciel(p)):
            res+=1
    
    print(res)




    