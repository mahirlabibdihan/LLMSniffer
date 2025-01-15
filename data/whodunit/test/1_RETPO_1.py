# Coding is about expressing your feeling and there is always a better way to express your feeling _feelme
import sys,math,numpy as np
# sys.stdin,sys.stdout=open('input.txt','r'),open('output.txt','w')
from sys import stdin,stdout;mod=int(1e9 + 7);from statistics import mode
from collections import deque,defaultdict;from math import ceil,floor,inf,factorial,gcd,log2
ii1=lambda:int(stdin.readline().strip())
is1=lambda:stdin.readline().strip()
iia=lambda:list(map(int,stdin.readline().strip().split()))
isa=lambda:stdin.readline().strip().split()
# print('{:.3f}'.format(1),round(1.123456789,4))
# np.set_printoptions(sign=' ',legacy='1.13') # legacy add space at sign position
def lcm(a,b): return (a*b)//gcd(a,b)
def setbits(n):return bin(n).count('1')
def resetbits(n):return bin(n).count('0')
def modinv(n,p):return pow(n,p-2,p)
def ncr_p(n, r, p):
    num,den=1,1;
    for i in range(r):num = (num * (n - i)) % p ;den = (den * (i + 1)) % p
    return (num * modinv(den,p)) % p
def isPrime(num) :
    if num<=1:return False
    if num==2 or n==3:return True
    if (num % 2 == 0 or num % 3 == 0) :return False
    for i in range(5,int(num**0.5)+1,6):
        if (num % i == 0 or num % (i + 2) == 0) :return False
    return True
def bin_search(arr, low, high, val):
    while low <= high:
        mid = low + (high - low) // 2;
        if arr[mid] == val:return mid
        elif arr[mid] < val:low = mid + 1
        else:high = mid - 1
    return -1
def sumofdigit(num):
    count=0;
    while num : count+=num % 10;num //= 10
    return count;
def make_dic(arr):
    freq = {}
    for val in arr : freq[val] = (freq[val] + 1 if val in freq else 1)
    # print(freq)
    return freq
def inputmatrix():
    r,c=iia();mat=[0]*r;
    for i in range(r):mat[i]=iia();
    return mat;
def prefix_sum(n,arr):
    for i in range(1,n):arr[i]+=arr[i-1]
    return arr;
def binomial(n, k):
    if 0 <= k <= n:
        ntok = 1;ktok = 1
        for t in range(1, min(k, n - k) + 1):ntok *= n;ktok *= t;n -= 1
        return ntok // ktok
    else:return 0
def divisors(n):
    res = [];
    for i in range(1,ceil(sqrt(n))+1):
        if n%i == 0:
            if i==n//i:res.append(i)
            else:res.append(i);res.append(n//i)
    return res;
# code here ----->
for _ in range(ii1()):
    n,m=iia()
    if abs(n)==abs(m):
        print(abs(n)+abs(m))
        continue
    elif abs(n)>abs(m):
        if (abs(n)-abs(m))&1:
            print(2*abs(n)+1)
        else:
            print(2*abs(n))
    else:
        if (abs(m)-abs(n))&1:
            print(2*abs(m)-1)
        else:
            print(2*abs(m))


