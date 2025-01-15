# Imports
from sys import stdin,stdout 
import math 
from collections import Counter  
import functools 
import time 
##########################################
# DEFINITIONS
def tr():
    return range(int(line()))

def sm():
    return map(int,line().split())

def ln():
    return list(sm())

def nl():
    return int(line())

def ssm():
    return map(str,line().split())

def line():
    return stdin.readline().rstrip()

def b(x):
    return bin(x).replace("0b","")

def o(x):
    if type(x) != type(""):
        x = str(x)
    stdout.write(x + "\n")
def osp(x):
    if type(x) != type(""):
        x = str(x)
    stdout.write(x + " ")
def ol(x):
    stdout.write(" ".join(map(str,x)))


##########################################
# Main Code and Functions 

def checkPalindrome(s):
    return s == s[::-1]
def main():
    for _ in tr():
        s = line()
        if checkPalindrome(s):
            print("YES")
            continue 
        possible = False
        n = len(s)
        for i in range(n//2):
            if s[i]!=s[n-i-1]:
                if checkPalindrome(s[:i] + s[i+1:]):
                    possible = True 
                elif checkPalindrome(s[:n-i-1]+s[n-i:]):
                    possible = True 
                else:
                    break
        print("YES" if possible else "NO")
                
                
        
    
main()
