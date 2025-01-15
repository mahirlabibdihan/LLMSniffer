t = int(input())
for i in range(0,t):
    s=input()
    l = list(s)
    sum = 0
    for i in l:
        if i.isdigit():
            sum += int(i)
    print(sum)
