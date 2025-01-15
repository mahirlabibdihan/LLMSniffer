import sys
import math
from collections import defaultdict,Counter,deque
import os
import sys
from io import BytesIO, IOBase

sys.setrecursionlimit(1000000009)

BUFSIZE = 8192
MOD = 1000000007

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

def isPrime(x):
    for i in range(2,x):
        if i*i>x:
            break
        if (x%i==0):
            return False
    return True

def ncr(n, r, p):  
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,p - 2, p)) % p

def power(x, y, p) : 
    res = 1
    x = x % p 
    if (x == 0) : 
        return 0
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
        y = y >> 1   # y = y/2 
        x = (x * x) % p         
    return res 

def debug(**kwargs):
    for i in kwargs:
        print(f'[{i} = {kwargs[i]}]', end = ' ', file = sys.stderr)
    print(file = sys.stderr)

try:
    sys.stdin = open('C:\\Users\\admin\\Desktop\\python programs\\CP\\input.txt', 'r+')
    sys.stdout = open('C:\\Users\\admin\\Desktop\\python programs\\CP\\output.txt', 'w+')
    sys.stderr = open('C:\\Users\\admin\\Desktop\\python programs\\CP\\error.txt', 'w+')
except:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

inp = lambda: sys.stdin.readline().rstrip()
iinp = lambda : int(inp())
minp = lambda type, splt = ' ': map(type, inp().split(splt))
linp = lambda type, splt = ' ': list(minp(type, splt))
dict = lambda type: defaultdict(type)

def solve():
    n, k = minp(int)
    l = [chr(i) for i in range(97, 97 +26)]
    if n > k:
        print('-1')
        return
    # n >= k
    if n == k:
        print('a' * n)
        return
    else:
        a = [1] * n
        total = n

        for i in range(n - 1, -1, -1):
            while total + a[i] <= k:
                total += a[i]
                # a[i] <<= 1
                a[i] *= 2
        if total != k:
            print('-1')
            return
        else:
            # logarithms
            for i in range(n):
                index = int(math.log(a[i], 2))
                print(l[index], end = '')
            print()






t = 1
t = iinp()

for _ in range(t):
    solve()


exit(0)