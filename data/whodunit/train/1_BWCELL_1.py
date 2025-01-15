t = int(input())

for i in range(t):
    s = input()
    n = len(s)
    p = s.find('W')
    l = p
    r = n - p - 1
    if l != 0 and r != 0:
    	if l != r:
        	print('Aleksa')
    	else:
        	print('Chef')
    elif l == 0 and r != 0:
    	print('Aleksa')
    elif l != 0 and r == 0:
     	print('Aleksa')
    else:
     	print('Chef')   