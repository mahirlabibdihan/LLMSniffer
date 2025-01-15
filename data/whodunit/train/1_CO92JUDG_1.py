def  call():
    n = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    tA = sum(A)-max(A)
    tB = sum(B)-max(B)
    if(tA<tB):
        print("Alice")
    elif(tB<tA):
        print("Bob")
    else:
        print('Draw')
        
t = int(input())
for i in range(t):
    call()