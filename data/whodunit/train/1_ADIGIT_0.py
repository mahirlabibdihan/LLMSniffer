nums,cases= map(int,input().split())

inpL = list(map(int,list(input().strip())))
popn = [[]for i in range(10)] #differences in all possible pairs of 1 to 9

for n in range(10):
 myBin=0
 for j in inpL:
  myBin+=abs(int(j)-n)
  popn[n]+=[myBin]
 
for c in range(cases):
 q=int(input())
 queried=inpL[q-1]
 print(popn[int(queried)][q-1])