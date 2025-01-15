
import bisect, sys


MAX = 1000000

if __name__ == '__main__':
	N, K = list(map(int, sys.stdin.readline().split()))
	T = list(map(int, sys.stdin.readline().split()))
	L, R = {}, {}

	for i, x in enumerate(T):
		if x not in L:
			L[x] = i
		R[x] = i


	T = frozenset(T)
	min_idx = N

	for x in sorted(T):
		if 2 * x >= K:
			break
		elif (K - x) in T:
			min_idx = min(min_idx, max(L[x] + 1, L[K - x] + 1))
			min_idx = min(min_idx, max(L[x] + 1, N - R[K - x]))
			min_idx = min(min_idx, max(N - R[x], N - R[K - x]))
			min_idx = min(min_idx, max(N - R[x], L[K - x] + 1))

	print(min_idx if min_idx < N else -1)