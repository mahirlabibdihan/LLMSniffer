def solve():
    s = input()
    if len(s) != 5:
        print("Error")
    else:
        if (s[0] < 'a' or s[0] > 'h') or (s[1] < '1' or s[1] > '8') or (s[2] != '-') or (s[3] < 'a' or s[3] > 'h') or (
                s[4] < '1' or s[4] > '8'):
            print("Error")
        else:
            c1 = ord(s[0])
            c2 = ord(s[3])
            d1 = int(s[1])
            d2 = int(s[4])
            if abs((c1 - c2) * (d1 - d2)) == 2:
                print("Yes")
            else:
                print("No")
                

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        solve()
        t -= 1
