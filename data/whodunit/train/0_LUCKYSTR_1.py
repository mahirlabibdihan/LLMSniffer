def is_good_string(string, fav_strings):
    if len(string) >= 47:
        return "Good"
    for fav in fav_strings:
        if fav in string:
            return "Good"
    return "Bad"

K, N = map(int, input().split())
fav_strings = [input() for _ in range(K)]
found_strings = [input() for _ in range(N)]

for string in found_strings:
    print(is_good_string(string, fav_strings))