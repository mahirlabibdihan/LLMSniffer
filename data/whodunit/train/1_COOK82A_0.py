for scenario in range(int(input())):
    teams = dict()
    for i in range(4):
        key, val =  input().strip().split()
        teams[key] = int(val)
    print('Barcelona') if teams['Barcelona']>teams['Eibar'] and teams['RealMadrid']<teams['Malaga'] else print('RealMadrid')