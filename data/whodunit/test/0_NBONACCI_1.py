def xor_n_bonacci(n, q, f, k_list):
    xor = [0]*3*n
    xor[:n] = f
    for i in range(n, 3*n):
        xor[i] = xor[i-n] ^ xor[i-1]
    for k in k_list:
        print(xor[(k-1)%(2*n)])

n, q = map(int, input().split())
f = list(map(int, input().split()))
k_list = [int(input()) for _ in range(q)]
xor_n_bonacci(n, q, f, k_list)