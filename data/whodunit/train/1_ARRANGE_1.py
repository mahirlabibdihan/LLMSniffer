from math import *
form = lambda x : int(x) if x.isdigit() else x
def padBin(n, k):
    b = bin(n)[2:]
    return ("0"*(ceil(len(b)/k)*k-len(b))) + b
def revBin(n, k):
    return int(padBin(n,k)[::-1], 2)
    
test=int(input())
for _ in range(test):
    k, mes = map(form, input().split())
    scrambled = ['']*(2**k)
    for i in range(2**k):
        scrambled[revBin(i,k)] = mes[i]
    print (''.join(scrambled))