from audioop import reverse

from itertools import count
from math import*
from operator import index, indexOf
from pickle import TRUE
from re import M, T


# # def bs(x, k, a):
# #     r = a-1
# #     l = 0
# #     while(l < r):
# #         m = (l+r)//2
# #         if((x >= k[m] and x < k[m+1]) or (m == a-1 and x > k[m+1])):
# #             return m+1
# #         elif(x < k[m]):
# #             r = m
# #         else:
# #             l = m+1
# #     return 0


# def check(nums):
#     for i in range(len(nums)-1):
#         if nums[i] > nums[i+1]:
#             return False
#     return True

def rl():
    return list(map(int, input().split()))


def r2():
    return map(int, input().split())


def func(x):
    l = len(str(x))
    e = str(x).count('8')
    f = str(x).count('5')
    t = str(x).count('3')
    y = e+f+t
    return e >= f and f >= t and y == l


# def Count(s, c):
#     j = 0
#     for i in s:
#         if i == c:
#             j += 1
#     return j

def solve(n, arr):
    m = 0
    for i in range(n):
        if func(arr[i]):
            m += 1

    return m


if __name__ == "__main__":
    res = []
    a = []
    n = int(input())
    for i in range(n):
        arr = list(input().split())
        a.append(arr[-1])

    print(solve(n, a))
