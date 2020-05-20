CHICKEN_PRICE = 23
GOAT_PRICE = 678
PIG_PRICE = 1296
COW_PRICE = 3848
SHEEP_PRICE = 6769

user_money = int(input())


def pluralize_name(name):
    if name != 'sheep':
        return name + 's'
    else:
        return name


def sell(product_name, unit_price, money_available):
    quantity = money_available // unit_price
    if quantity > 1:
        product_name = pluralize_name(product_name)
    print(str(quantity) + ' ' + product_name)


if user_money >= SHEEP_PRICE:
    sell('sheep', SHEEP_PRICE, user_money)
elif user_money >= COW_PRICE:
    sell('cow', COW_PRICE, user_money)
elif user_money >= PIG_PRICE:
    sell('pig', PIG_PRICE, user_money)
elif user_money >= GOAT_PRICE:
    sell('goat', GOAT_PRICE, user_money)
elif user_money >= CHICKEN_PRICE:
    sell('chicken', CHICKEN_PRICE, user_money)
else:
    print('None')
