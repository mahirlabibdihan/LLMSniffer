
def run():
    T = int(input())
    for _ in range(T):
        N = int(input())
        polygons = []
        for i in range(N):
            M = int(input())
            polygon = list(map(int, input().split()))
            polygons.append(polygon)
        print(f(polygons))
        
def f(polygons):
    highest = []
    for i, polygon in enumerate(polygons):
        hi = float('-inf')
        for x in range(0, len(polygon), 2):
            px, py = polygon[x], polygon[x+1]
            hi = max(hi, py)
        highest.append((i, hi))
    
    highest = sorted(highest, key=lambda x: x[1])
    ans = [0] * len(polygons)
    for n, (i, hi) in enumerate(highest):
        ans[i] = str(n)
    return " ".join(ans)
        
if __name__ == "__main__":
    
    run()

