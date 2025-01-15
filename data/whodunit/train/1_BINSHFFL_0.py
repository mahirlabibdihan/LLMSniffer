for t in range(int(input())):
	A, B = map(int, input().split(" "))
	countA, countB = (str(bin(A)).count("1"), str(bin(B-1)).count("1"))
	if A==B:
		print("0")
	elif A!=0 and (B==0 or B==1):
		print("-1")
		pass
	elif(countA>countB):
		print("2")
		pass
	else:
		print(countB-countA+1)