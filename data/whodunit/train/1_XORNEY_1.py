import sys
from sys import stdin,stdout
def get_int():return int(stdin.readline().strip())
def get_ints():return map(int,stdin.readline().strip().split())
def op(c):return stdout.write(c+"\n") 
t=get_int()
for _ in range(t):
    l,r=get_ints()
    n=(r-l)//2
    if (r % 2 != 0 or l % 2 != 0): 
        n += 1 
    if n%2==0:
        op("Even")
    else:
        op("Odd")
    
