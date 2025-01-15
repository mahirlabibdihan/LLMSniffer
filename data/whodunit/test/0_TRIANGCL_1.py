import math

def classify_triangle(x1, y1, x2, y2, x3, y3, subtask_id):
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)

    sides = sorted([a, b, c])
    angles = sorted([math.degrees(math.acos((sides[0]**2 + sides[1]**2 - sides[2]**2) / (2 * sides[0] * sides[1]))) for _ in range(3)])

    if subtask_id == 1:
        if sides[0] == sides[1] or sides[1] == sides[2]:
            return "Isosceles triangle"
        else:
            return "Scalene triangle"
    else:
        side_classification = "Isosceles" if sides[0] == sides[1] or sides[1] == sides[2] else "Scalene"
        angle_classification = "Acute" if angles[2] < 90 else "Right" if angles[2] == 90 else "Obtuse"
        return f"{side_classification} {angle_classification} triangle"

T = int(input())
for _ in range(T):
    subtask_id = int(input())
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    print(classify_triangle(x1, y1, x2, y2, x3, y3, subtask_id))