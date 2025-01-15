for i in range(int(input())):
    count=0
    l=list(map(int,input().split()))
    for num in l:
        if num==1:
            count+=1
    if count==0:
        print("Beginner")
    elif count==1:
        print("Junior Developer")
    elif count==2:
        print( "Middle Developer")
    elif count==3:
        print("Senior Developer")
    elif count==4:
        print("Hacker")
    elif count==5:
        print( "Jeff Dean")