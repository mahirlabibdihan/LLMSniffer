import math as mt
test_case=int(input())
for test in range(test_case):
    n = int(input());
    x = int(mt.sqrt(n));
    remainder = n - x * x
    x1 = x2 = d1 = 0
    x1 += x
    x1 += remainder // x
    remainder = n % x
    string = "X" * x1 + "D" * (x - remainder) + "X"*(remainder>0) + "D" *(remainder)
    print(string)