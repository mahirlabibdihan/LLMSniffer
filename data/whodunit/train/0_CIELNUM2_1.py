def is_ciel(num):
    num = str(num)
    return all(digit not in num for digit in ['0', '1', '2', '4', '6', '7', '9']) and num.count('8') >= num.count('5') >= num.count('3')

N = int(input().strip())
count = sum(1 for _ in range(N) if is_ciel(int(input().strip().split()[1])))
print(count)