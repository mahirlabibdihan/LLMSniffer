T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    unique_elements = set(A)
    max_count = 0
    max_element = None
    for element in unique_elements:
        count = A.count(element)
        if count > max_count or (count == max_count and element < max_element):
            max_count = count
            max_element = element
    print(max_element, max_count)