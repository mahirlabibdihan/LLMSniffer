MD = 998244353
N = int(input())
a = 2
b = 1
for n in range(2,N+1):
	a,b = (a*(2*n-1) + 2*b)%MD, b*(2*n-1)%MD
# endfor n
bd = pow(b,MD-2,MD)
r = a*bd%MD
print (r)
