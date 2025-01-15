def EstimateSkill(points) :
    count = points.count(1)
    
    if count == 0:
        return "Beginner"
    elif count == 1:
        return "Junior Developer"
    elif count == 2:
        return "Middle Developer"
    elif count == 3:
        return "Senior Developer"
    elif count == 4:
        return "Hacker"
    else:
        return "Jeff Dean"
    
    
LIMIT = int(input()) 

while LIMIT > 0 :
    LIMIT -= 1 
    points = list(map(int, input().split()))
    print(EstimateSkill(points))