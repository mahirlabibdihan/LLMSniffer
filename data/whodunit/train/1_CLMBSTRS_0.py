
##########################################
# DEFINITIONS
def trange():
	return range(int(input()))

def splitMap():
	return map(int,input().split())

def listOfNumbers():
	return list(map(int,input().split()))

def number():
	return int(input())


def binary(x):
	return bin(x).replace("0b","")

##########################################
import math 
from collections import Counter  
import functools 

def main():
	# PreCompute Fibonacci 
	fibonaci = [1,2]
	modulo = 10**9  + 7
	maxN = 10**6
	for i in range(maxN):
	    fibonaci.append((fibonaci[-1]+fibonaci[-2])%modulo) 
	for _ in trange():
		numberOfStairs, villageGuess = splitMap()
		m = fibonaci[numberOfStairs-1]
		correctGuess = binary(m).count('1')
		if  correctGuess == villageGuess:
			print("CORRECT")
		else:
			print("INCORRECT")


if __name__ == '__main__':
	main()
	exit()