for i in range(int(input())):
    m,n = map(int,input().split())
    a = input().split()
    for i in range(n):
        coin = a.pop()
        if coin == 'H':
            for j in range(len(a)):
                if a[j] == 'H' : a[j] = 'T'
                else: a[j] = 'H'
    print(a.count('H'))