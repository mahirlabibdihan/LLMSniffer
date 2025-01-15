# by David Ham
from sys import stdin, stdout
# Faster I/O ======================
pr = lambda i : stdout.write(f'{i}\n')
inp = lambda : stdin.readline().strip()
im = lambda : map(int, stdin.readline().strip().split()) # int map
# =================================
def main():
    t = int(inp())
    for _ in range(t):
        n, m = im()
        prevrow = ''
        s = 'yes'

        for i in range(n):
            row = inp()
            if s == 'yes':
                if row[0] == 'W' or row[-1] == 'W' or 'WA' in row or 'AW' in row:
                    s = 'no'
                    continue

                if prevrow:
                    for pval, nval in zip(prevrow, row):
                        if (pval == 'B' and nval == 'A') or (pval == 'B' and nval == 'W') or (pval == 'W' and nval == 'A'):
                            s = 'no'
                            break
                
                prevrow = row

        pr(s)
# =================================
if __name__ == '__main__':
    main()
