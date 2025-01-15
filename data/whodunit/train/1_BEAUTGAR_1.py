for _ in range(int(input())):
    string=input()
    if(len(string) % 2 == 1):
        print("no")
    elif(string.count('R') != string.count('G')):
        print("no")
    else:
        count=0
        for i in range(1,len(string)):
            if(string[i] == string[i-1]):
                count+=1
        if(count<=2):
            print("yes")
        else:
            print("no")        
        