def min_troops(T, H_list):
    result = []
    for i in range(T):
        H = H_list[i]
        result.append(H.count('a') > 0 and H.count('b') > 0)
    return result

T = int(input().strip())
H_list = [input().strip() for _ in range(T)]
print('\n'.join(map(str, min_troops(T, H_list))))