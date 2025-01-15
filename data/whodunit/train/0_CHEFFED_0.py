def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def solve(n):
    count = 0
    for x in range(max(1, n - 100), n):
        if x + sum_of_digits(x) + sum_of_digits(sum_of_digits(x)) == n:
            count += 1
    return count

n = int(input())
print(solve(n))