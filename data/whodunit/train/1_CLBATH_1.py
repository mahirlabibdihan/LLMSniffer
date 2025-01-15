import sys

t = int(input())

while (t):

	line = input().split()
	v1,t1, v2,t2, v3,t3 = int(line[0]),int(line[1]), int(line[2]),int(line[3]), int(line[4]),int(line[5])

	if (t3 < t1 or t3 > t2):
		sys.stdout.write('NO\n')
	else:
		if (v3*(t3-t2)/(t1-t2) > v1):
			sys.stdout.write('NO\n')
		elif (v3*(t1-t3)/(t1-t2) > v2):	
			sys.stdout.write('NO\n')
		else:
			sys.stdout.write('YES\n')

	t -= 1