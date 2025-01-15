for i in range(int(input())):
	string = input()
	pos = -1
	res = 0

	for i in range(len(string)):
		if string[i] == '4':
			pos = i
		if pos != -1:
			res += pos + 1

	print(res)
