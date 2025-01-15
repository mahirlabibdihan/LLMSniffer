def find_smallest_number(n, arr):
    for i in arr:
        while i % 10 == 0:
            i //= 10
        while i % 2 == 0:
            i //= 2
        while i % 5 == 0:
            i //= 5
        print(i)

n = int(input())
arr = [int(x) for x in input().split()]
find_smallest_number(n, arr)