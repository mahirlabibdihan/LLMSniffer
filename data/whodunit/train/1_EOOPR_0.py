# Take input for the number of test cases
number_of_test_cases = int(input())

# Loop through each test case
for _ in range(number_of_test_cases):
    # Take input for the values x and y
    x, y = [int(inp) for inp in input().split()]
    
    # Calculate the difference between y and x
    difference = y - x
    
    # Check if the difference is even
    is_even = difference % 2 == 0
    
    # Check different cases and print the result
    if difference == 0:
        print(0)  # No operations needed if the values are the same
    elif difference > 0:
        if is_even and difference % 4 == 0:
            print(3)  # Special case: difference is even and divisible by 4
        elif is_even:
            print(2)  # Difference is even
        else:
            print(1)  # Difference is odd
    else:
        if is_even:
            print(1)  # Difference is negative but even
        else:
            print(2)  # Difference is negative and odd
