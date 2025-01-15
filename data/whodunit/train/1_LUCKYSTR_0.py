k, n = map(int,input().split())
a = list()
for i in range(k):
    s = input()
    a.append(s)
b = []
for i in range(n):
    s1 = input()
    b.append(s1)
for i in b:
    if len(i) >= 47:
        print('Good')
    else:
        for j in a:
            if j in i:
                print('Good')
                break
        else:
            print('Bad')