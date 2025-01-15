T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    if min(A, B) % 2 == 0:
        print("Vanka")
    else:
        print("Tuzik")