for _ in range(int(input())):
	array = list(input().split())
	k = int(array[0])
	length = 2**k
	final = [0]*length
	for i in range(length):
		p = bin(i)[2:]
		for TT in range(k-len(p)):
			p = '0'+p
		p = p[-1::-1]
		final[int(p,2)] = array[1][i]
	print(''.join(final))