money, price = map(int,input().split())
print(f'거스름돈 : {money-price}')
print(f'500원 동전 개수 : {(money-price)//500}')
print(f'100원 동전 개수 : {((money-price)%500)//100}')