for _ in range(int(input())):
    n = int(input())
    checker = [0]*5
    for i in range(n):
        s = input()
        if s == "cakewalk":
            checker[0] = 1
        elif s == "simple":
            checker[1] = 1
        elif s == "easy":
            checker[2] = 1
        elif s == "easy-medium" or s == "medium":
            checker[3] = 1
        else:
            checker[4] = 1
            
    if sum(checker) == 5:
        print("Yes")
    else:
        print("No")