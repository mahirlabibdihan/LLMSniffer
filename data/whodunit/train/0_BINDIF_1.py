S = input().strip()
one_index = S.rfind('1')
A = S[:one_index] + '0' + '0' * (len(S) - one_index - 1)
B = '1' + '0' * (len(S) - one_index - 1)
print(A, B)