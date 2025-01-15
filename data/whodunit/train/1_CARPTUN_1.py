for T in range(int(input())):
	N = int(input())
	A = list(map(int, input().split()))
	C, D, S = map(int, input().split())
	delay = 0
	if C == 2:
		delay = max(A)
	else:
		delay = max(A)*(C-1)
	print(delay)