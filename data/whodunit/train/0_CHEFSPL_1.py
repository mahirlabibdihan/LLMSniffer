def is_special(dish):
    dish_length = len(dish)
    for i in range(dish_length):
        temp_dish = dish[:i] + dish[i+1:]
        if temp_dish[:len(temp_dish)//2] == temp_dish[len(temp_dish)//2:]:
            return "YES"
    return "NO"

D = int(input().strip())
for _ in range(D):
    dish = input().strip()
    print(is_special(dish))