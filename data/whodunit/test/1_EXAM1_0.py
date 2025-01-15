for _ in range(int(input())):
	score = 0
	n = int(input())
	corr = input()
	resp = input()
	i = 0
	
	while i < n:
		if resp[i] == 'N':
			i += 1
		elif corr[i] == resp[i]:
			score += 1
			i += 1
		else:
			i += 2
		
	print(score)