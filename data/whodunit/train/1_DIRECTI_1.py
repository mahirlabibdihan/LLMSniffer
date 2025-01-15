t=int(input())
for i in range(t):
    n=int(input())
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    
    dict1={}
    dict1={"Right":"Left","Left":"Right"}
    for i in range(n):
        a=[]
        a=list(input().split())
        list7=[]
        str1=""
        str2=""
        str3=" "
        str1+=a[0]
        list7=a[2:]
        str2=str3.join(list7)
        
        list1.append(str1)
        list2.append(str2)
    list3=list1[1:]
    list4=list2[:len(list2)-1]
    list5=list3[::-1]
    list6=list4[::-1]
    print("Begin on",end=" ")
    print(list2[-1])
    for i in range(n-1):
        print(dict1[list5[i]],end=" ")
        print("on",end=" ")
        print(list6[i])
        
        
    
