def count_number_of_odd_pairs(A,B):
    count_of_A_odd_numbers = len([x for x in A if x % 2 != 0])
    count_of_B_odd_numbers = len([x for x in B if x % 2 != 0])
    
    count_of_A_even_numbers = len(A) - count_of_A_odd_numbers
    count_of_B_even_numbers = len(B) - count_of_B_odd_numbers
    

    return min(count_of_A_odd_numbers,count_of_B_odd_numbers) + min(count_of_A_even_numbers, count_of_B_even_numbers)

def calculate_max_height_of_children(A,B):
    number_of_odd_pairs = len(A) - count_number_of_odd_pairs(A,B)
    averageOfPairs = (sum(A) + sum(B))/ 2
    return int(averageOfPairs - (number_of_odd_pairs*0.5))

t=int(input())
for i in range(t):
    n=int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    print(calculate_max_height_of_children(A,B))