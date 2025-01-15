jacketCost, sockCost, money = map(int, input().split())
remaining_money = money - jacketCost
socks_bought = remaining_money // sockCost
if socks_bought % 2 == 0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")