from math import floor, ceil

black = 1
red = 0

for _ in range(int(input())):

	query = input().split()
	path = [0, 0]

	if query[0] == 'Qi':
		black, red = red, black
		continue

	x = int(query[1])
	y = int(query[2])

	if (x < y):
		x, y = y, x

	while len(bin(x)) != len(bin(y)):
		path[len(bin(x))%2] += 1
		x = floor(x/2)
		
	while x!=y:
		path[len(bin(x))%2] += 1
		path[len(bin(y))%2] += 1
		x, y = floor(x/2), floor(y/2)

	
	path[len(bin(x))%2] += 1

	if query[0] == 'Qb':
		print(path[black])
	else:
		print(path[red])