for _ in range(int(input())):
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    array_converter = list()
    for element in array:
        if element%k == 0:
            array_converter.append("1")
        else:
            array_converter.append("0")
    print(''.join(array_converter))
    