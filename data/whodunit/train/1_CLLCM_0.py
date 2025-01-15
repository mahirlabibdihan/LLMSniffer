
for _ in range(int(input())):
    a = int(input())
    b = list(map(int,input().split()))
    odd_num = list([i for i in b if i%2!=0])
    print("YES") if len(odd_num)==a else print("NO")