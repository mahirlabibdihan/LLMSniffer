K, N = map(int, input().split())
fav_strings = [input() for _ in range(K)]
found_strings = [input() for _ in range(N)]

for string in found_strings:
    if len(string) >= 47:
        print("Good")
    elif any(fav in string for fav in fav_strings):
        print("Good")
    else:
        print("Bad")