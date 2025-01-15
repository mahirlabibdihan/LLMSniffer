s=str(input().strip())
if s.count('1')==1:
    print(s,'0')
else:
    print('1'+'0'*len(s),'1'+'0'*s.count('0'))