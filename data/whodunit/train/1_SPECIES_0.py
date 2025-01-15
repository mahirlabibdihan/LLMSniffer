import math,sys,bisect,heapq,os
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
from functools import lru_cache
#sys.setrecursionlimit(200000000)
int1 = lambda x: int(x) - 1
def input(): return sys.stdin.readline().rstrip('\r\n')
#input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
aj = lambda: list(map(int, input().split()))
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])




def solve():

	d1 = [0,0,1,-1] 
	d2 = [1,-1,0,0]
	def ch1(x,y):
		if x < 0 or x >= n or y < 0 or y >= m:
			return False
		return True

	def ch2(x,y):
		if vis[x][y] or mat[x][y] != '?':
			return False
		return True


	def dfs(i,j):
		st = deque()
		st.append((i,j))
		C = Counter()
		C[mat[i][j]] = 1
		while st:
			x,y = st.pop()
			for i,j in zip(d1,d2):
				xx = x + i
				yy = y + j
				if ch1(xx,yy):
					if ch2(xx,yy):
						st.append((xx,yy))
						C[mat[xx][yy]] += 1
					if mat[xx][yy] in ['G','B','P']:
						C[mat[xx][yy]] = 1
					vis[xx][yy] = True
		return C


	for _ in range(int(input())):
		n,= aj()
		m= n
		mat = []
		for i in range(n):
			B = [*input()]
			mat.append(B)
		vis = [[False]*m for i in range(n)]
		ans = 1
		for i in range(n):
			for j in range(m):
				if not vis[i][j] and ch2(i,j) :
					vis[i][j] = True
					C = dfs(i,j)
					#print(C)
					if '?' in C:
						if len(C) == 4 or C['G'] == 1 or (len(C) == 3 and C['P'] == 1 and C['B'] == 1) :
							ans = 0;break
						elif len(C) == 1:
							if C['?'] == 1:
								ans*= 3
								ans %= MOD
							else:
								ans*=2
								ans %= MOD
			if ans == 0:
				break
		if ans != 0:
			for i in range(n):
				for j in range(m):
					if mat[i][j] in ['G','P','B']:
						for ii,jj in zip(d1,d2):
							x = ii + i
							y = jj + j
							if ch1(x,y):
								if mat[i][j] == 'G' and mat[x][y] in ['G','P','B','?']:
									ans = 0
									break
								elif mat[i][j] == 'P' and mat[x][y] in ['G','B']:
									ans = 0
									break
								elif mat[i][j] == 'B' and mat[x][y] in ['G','P']:
									ans = 0
									break
				if ans == 0:
					break
		print(ans%MOD)



try:
	#os.system("online_judge.py")
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')
except:
	pass

solve()
