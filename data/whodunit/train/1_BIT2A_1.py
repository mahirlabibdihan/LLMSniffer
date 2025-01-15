try:
    Test_Case=int(input())
    for i in range(Test_Case):
        N=int(input())
        list1=list(map(int,input().split(" ")))
        list2=[]
        if(len(list1)==N):
                for k in range(len(list1)):
                    c=0
                    for j in range(k+1,len(list1)):
                        if(list1[k]<list1[j]):
                            c=c+1
                        else:
                            continue
                            
                    list2.append(c)
        for l in range(len(list2)):
            print(list2[l],end=" ")
                
except:
    pass
