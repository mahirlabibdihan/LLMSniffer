for _ in range(int(input())):
    n,m=map(int,input().split(" "))
    l=[]
    temp=""
    temp2=""
    find=False
    for i in range(n):
        word=input()
        word=word.lower()
        #print(word,len(word))
        temp=temp+" "+word
        temp2=temp2+word
    if(temp.find("spoon")!=-1):
        find=True
    if(n>4):
        for i in range(m):
            w=temp2[i::m]
            if(w.find("spoon")!=-1):
                find=True
    if(find==True):
        print("There is a spoon!")
    else:
        print("There is indeed no spoon!")
        
    