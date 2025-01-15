for _ in range(int(input())):
    lst = []
    choice = 0
    #print("Enter the values of d, u and n")
    d, u, n = map(float, input().split())
    check = d*u
    #print("Enter the ",int(n), "lines containing m, r and c")
    for i in range(int(n)):
        m, r, c = map(float, input().split())
        #check1 = (c + (m*r*u))/m
        check1 = (c/m) + (r*u)
        if check> check1:
            check = check1
            choice = i+1
    print(choice)
