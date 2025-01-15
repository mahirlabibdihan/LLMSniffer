def is_knight_move(move):
    if len(move) != 5 or move[2] != '-':
        return "Error"
    start, end = move[:2], move[3:]
    if not ('a' <= start[0] <= 'h' and '1' <= start[1] <= '8') or not ('a' <= end[0] <= 'h' and '1' <= end[1] <= '8'):
        return "Error"
    dx, dy = abs(ord(start[0]) - ord(end[0])), abs(int(start[1]) - int(end[1]))
    return "Yes" if (dx, dy) in [(1, 2), (2, 1)] else "No"

T = int(input().strip())
for _ in range(T):
    move = input().strip()
    print(is_knight_move(move))