for _ in range(int(input())):
	n = int(input())
	li = [int(i) for i in input().split()]
	d = n*(n-1)/2
	ma = 0
	l = 0
	for i in range(n):
		if li[i]>=ma:
			if li[i]==ma:
				l+=1
			else:
				ind = i
				ma = li[i]
				l = 1
	if l>1:
		s=l*(l-1)/2
	else:
		a = max(li[:ind]+li[ind+1:])
		s = li.count(a)
	print(f'{s/d:.8f}')