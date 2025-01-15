try:
    for _ in range(int(input())):
        n,k=map(int,input().split())
        if(n%2==0 or k%2==0):
            print('Tuzik')
        else:
            print('Vanka')
except:
    pass