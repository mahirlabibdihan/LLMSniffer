def is_special(dish):
    dish_length = len(dish)
    for i in range(dish_length):
        temp_dish = dish[:i] + dish[i+1:]
        half = len(temp_dish) // 2
        if temp_dish[:half] == temp_dish[half:]:
            return "YES"
    return "NO"

D = int(input().strip())
for _ in range(D):
    dish = input().strip()
    print(is_special(dish))