colConv = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

col = set(list('abcdefgh'))
row = set(list('12345678'))
for _ in range(int(input())):
    m = input()
    if len(m) != 5:
        print ("Error")
        continue
    if (m[2] != '-') or (m[0] not in col) or (m[3] not in col) or (m[1] not in row) or (m[4] not in row):
        print ("Error")
        continue
    x1, y1, x2, y2 = colConv[m[0]], int(m[1]), colConv[m[3]], int(m[4]) 
    if ((abs(x1-x2) == 2 and abs(y1-y2) == 1) or (abs(x1-x2) == 1 and abs(y1-y2) == 2)):
        print ("Yes")
    else:
        print ("No")