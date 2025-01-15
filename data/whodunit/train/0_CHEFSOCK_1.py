def chef_luck(jacketCost, sockCost, money):
    remaining_money = money - jacketCost
    socks_bought = remaining_money // sockCost
    return "Lucky Chef" if socks_bought % 2 == 0 else "Unlucky Chef"

jacketCost, sockCost, money = map(int, input().split())
print(chef_luck(jacketCost, sockCost, money))