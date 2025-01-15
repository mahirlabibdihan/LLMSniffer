import cmath
T = int(input())
for _ in range(T):
    R, L, C, Vin = map(int, input().split())
    s = R / (2 * L)
    Vout = Vin / cmath.sqrt(1 + (s * L - 1 / (s * C)) ** 2)
    print(Vin / Vout.real)