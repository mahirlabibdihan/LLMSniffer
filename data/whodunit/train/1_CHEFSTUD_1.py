try:
    t = int(input())
    for _ in range(t):
    	s = input()
    	l = ""
    	for i in s:
    		if i=='>':
    			l += '<'
    		elif i=='<':
    			l += '>'
    		else:
    			l += i
    	print(l.count("><"))
except:
    pass