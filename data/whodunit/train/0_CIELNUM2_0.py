def is_ciel(num):
    num = str(num)
    for digit in ['0', '1', '2', '4', '6', '7', '9']:
        if digit in num:
            return False
    return num.count('8') >= num.count('5') >= num.count('3')

N = int(input().strip())
count = 0
for _ in range(N):
    menu, price = input().strip().split()
    price = int(price)
    if is_ciel(price):
        count += 1
print(count)