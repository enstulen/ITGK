__author__ = 'Morten Stulen'
teeth = [95, 103, 71, 99, 114, 64, 95, 53, 97, 114, 109, 11, 2, 21, 45, 2, 26, 81, 54, 14, 118, 108, 117, 27, 115, 43, 70, 58, 107]

twenty_coins, ten_coins, five_coins, one_coins, half_coin = 0, 0, 0, 0, 0
twenty_coins_total, ten_coins_total, five_coins_total, one_coins_total, half_coin_total = 0, 0, 0, 0, 0

for i in range(0, len(teeth)):
    money_amount = float(teeth[i] * 0.5)
    if money_amount/20 >= 1:
        twenty_coins = money_amount//20
        money_amount = money_amount - twenty_coins * 20
    if money_amount/10 >= 1:
        ten_coins = int(money_amount/10)
        money_amount = money_amount - ten_coins * 10
    if money_amount/5 >= 1:
        five_coins = int(money_amount/5)
        money_amount = money_amount - five_coins * 5
    if money_amount/1 >= 1:
        one_coins = int(money_amount/1)
        money_amount = money_amount - one_coins * 1
    if money_amount == 0.5:
        half_coin = 1
    else:
        half_coin = 0

    twenty_coins_total += twenty_coins
    ten_coins_total += ten_coins
    five_coins_total += five_coins
    one_coins_total += one_coins
    half_coin_total += half_coin

    print("For barn nr: %d trengs det (%s) 20-kroninger, (%s) 10-kroninger, (%s) 5-kroninger, (%s) 1-kroninger og (%s) 50-øringer" % ((i + 1), twenty_coins, ten_coins, five_coins, one_coins, half_coin))
print("\n" "Tilsammen må det tas med (%s) 20-kroninger, (%s) 10-kroninger, (%s) 5-kroninger, (%s) 1-kroninger og (%s) 50-øringer" % (twenty_coins_total, ten_coins_total, five_coins_total, one_coins_total, half_coin_total))

