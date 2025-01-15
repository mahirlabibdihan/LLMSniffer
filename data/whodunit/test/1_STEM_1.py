import sys

T = int(sys.stdin.readline())

for t in range(T):
    n = int(sys.stdin.readline())
    w = sys.stdin.readline().strip()
    
    words = w.split()
    shortest_word = min(words, key=len)
    
    longest_substr_len = 0
    longest_substr = ""
    
    for i in range(0, len(shortest_word)):
        for j in reversed(range(i + 1, len(shortest_word) + 1)):
            sub_str = shortest_word[i:j]
            found = True
            for word in words:
                if sub_str not in word:
                    found = False
                    break
    
            if found:
                if len(sub_str) > longest_substr_len:
                    longest_substr_len = len(sub_str)
                    longest_substr = sub_str
                elif len(sub_str) == longest_substr_len:
                    if sub_str < longest_substr:
                        longest_substr_len = len(sub_str)
                        longest_substr = sub_str
    
    print(longest_substr)

