a=str(input().strip())
if a.count('1')==1:
    print(a,'0')
else:
    print('1'+'0'*len(a),'1'+'0'*a.count('0'))