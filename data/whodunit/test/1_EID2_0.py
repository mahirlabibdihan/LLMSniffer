for _ in range(int(input())):
	li = [int(i) for i in input().split()]
	li1 = [(li[i],li[i+3]) for i in range(3)]
	li1.sort()
	for i in range(2):
		a= li1[i][0]-li1[i+1][0]
		b =li1[i][1]-li1[i+1][1]
		if (a>0 and b>0) or (a==0 and b==0) or (a<0 and b<0):
			continue
		print("NOT FAIR")
		break
	else:
		print("FAIR")