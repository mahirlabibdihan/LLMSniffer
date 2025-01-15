
for _ in range(int(input())):
    n=input()
    if n.count('1')==0:
        print('NO')
        continue
    for i in range(len(n)-2):
        if n[i]=='1' and n[i+1]=='0' and '1' in n[i+2:]:
            print('NO')
            break
    else:
        print('YES')
