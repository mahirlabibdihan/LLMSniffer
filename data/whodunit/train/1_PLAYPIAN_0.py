for _ in range(int(input())):
    s = input()
    flag = True
    for i in range(0,len(s),2):
        if s[i:i+2]=="AA" or s[i:i+2]=="BB":
            flag = False
            break
    if flag==False:
        print("no")
    else:
        print("yes")
            
