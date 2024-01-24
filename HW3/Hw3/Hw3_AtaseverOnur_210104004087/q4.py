def coins_func(coins, amount):

    min_coins = float('inf') #To find min value, I will use this value to compare.
    if amount == 0: #if amount is zero it means one of possible coins is found so it makes min coin zero
        min_coins = 0
    for coin in coins:# It iterates all elements of coins
        if coin <= amount: #It only uses smaller or equal coins than amount 
           sub_amount = 1 + coins_func(coins, amount - coin) # If ıt finds zero it returnes zero else infinite
           min_coins = min(min_coins, sub_amount) #It founds smaller one and assign to min so it finds min number of coins
    return min_coins # It returns min

def main():
    coins = [5, 4, 15, 10]
    amount =20
    print(coins_func(coins, amount))

main()
