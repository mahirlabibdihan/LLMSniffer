for i in range(int(input())):
    N,name = input().split()
    N = int(N)
    list1 = list(map(int,input().split()))
    if (N==1 and name == "Dee" and list1[0]%2 == 0):
        print("Dee")
    else:
        print("Dum")
