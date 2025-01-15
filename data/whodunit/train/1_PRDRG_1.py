a = [int(x) for x in input().split()]
for i in range(a[0]):
    m1 = 1
    m2 = 1
    for x in range(3,a[i+1]+1):
        if x%2!=0:
            m1 = 2*m1 + m2
        else:
            m2 = 2*m2 + m1
    if a[i+1]%2==0:
        print(m2, end = " ")
    else:
        print(m1, end = " ")
    print(pow(2,a[i+1]), end = " ")