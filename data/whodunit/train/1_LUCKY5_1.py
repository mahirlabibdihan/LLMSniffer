t=int(input())
for i in range(t):
    n=raw_input().strip()
    print (len(n)-n.count('4')-n.count('7'))