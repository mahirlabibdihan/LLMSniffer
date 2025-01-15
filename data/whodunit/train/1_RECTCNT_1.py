#In the Name of God
import math

while(True):
	t = int(input())
	if(t == 0):
		break
	arr = [[0 for i in range(2)] for j in range(t)]

	for i in range(t):
		x = input().split()
		arr[i][0] = int(x[0])
		arr[i][1] = int(x[1])

	if t<4:
		print(0)
	else:
		arr.sort(key = lambda x : (x[0],x[1]))
		dict1 = {}

		i = 0
		while i < len(arr):
			if(i+1 < len(arr) and arr[i][0] == arr[i+1][0]):
				x = (arr[i][1],arr[i+1][1])
				if(x in dict1):
					dict1[x] += 1
				else:
					dict1[x] = 1
				i += 2
			else:
				i += 1
		sum = 0
		ele = list(dict1.values())
		for i in range(len(ele)):
			val = ((ele[i]-1)*ele[i])//2
			sum += val
		print(sum)