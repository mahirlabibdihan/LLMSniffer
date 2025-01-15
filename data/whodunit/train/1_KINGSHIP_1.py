#two options to solve this questions, first one is to assume the cities are nodes and form every possible vector
#edge as roads between the cities and find the MST of that graph
#Other approach is that the cost will be minimum if the minimum element of the cost is multiplied with every other one and added

test = int(input())
for _ in range(test):
    cities = int(input())
    array = sorted(list(map(int, input().split())))
    multiply = array[0]
    total=sum(array[1:])
    print(total*multiply)