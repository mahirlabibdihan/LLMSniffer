S = input().strip()
one_index = S.rfind('1')
A = S[:one_index] + '0' + S[one_index+2:]
B = '1' + S[one_index+1:]
print(A, B)