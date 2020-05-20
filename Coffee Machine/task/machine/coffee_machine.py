# Write your code here
class Beverage:
    beverages = []

    def __init__(self, water_needed, milk_needed, coffee_needed, price):
        self.water_needed = water_needed
        self.milk_needed = milk_needed
        self.coffee_needed = coffee_needed
        self.price = price
        Beverage.beverages.append(self)


espresso = Beverage(250, 0, 16, 4)
latte = Beverage(350, 75, 20, 7)
cappuccino = Beverage(200, 100, 12, 6)

money_stock = 550
water_stock = 400
milk_stock = 540
coffee_stock = 120
cups_stock = 9


def remaining():
    print(f"""
        The coffee machine has: 
        {water_stock} of water 
        {milk_stock} of milk 
        {coffee_stock} of coffee beans 
        {cups_stock} of disposable cups 
        {money_stock} of money
    """)


def choose_action():
    return input('Write action (buy, fill, take, remaining, exit):')


def choose_beverage():
    choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    if choice == 'back':
        return None

    return int(choice)


def check_stock(beverage):
    chosen_beverage: Beverage = Beverage.beverages[beverage - 1]
    if chosen_beverage.water_needed > water_stock:
        print('Sorry, not enough water!')
        return False

    if chosen_beverage.milk_needed > milk_stock:
        print('Sorry, not enough milk!')
        return False

    if chosen_beverage.coffee_needed > coffee_stock:
        print('Sorry, not enough coffee!')
        return False

    if cups_stock < 1:
        print('Sorry, not enough cups!')
        return False

    print('I have enough resources, making you a coffee!')
    return True


def brew(beverage):
    global money_stock, water_stock, coffee_stock, milk_stock, cups_stock
    enough_stock = check_stock(beverage)
    if enough_stock:
        chosen_beverage: Beverage = Beverage.beverages[beverage - 1]

        cups_stock -= 1
        water_stock -= chosen_beverage.water_needed
        coffee_stock -= chosen_beverage.coffee_needed
        milk_stock -= chosen_beverage.milk_needed
        money_stock += chosen_beverage.price


def take():
    global money_stock
    previous_stock = money_stock
    money_stock = 0
    print('I gave you $' + str(previous_stock))


def fill():
    global water_stock, milk_stock, coffee_stock, cups_stock

    water_stock += int(input('Write how many ml of water do you want to add:'))
    milk_stock += int(input('Write how many ml of milk do you want to add:'))
    coffee_stock += int(input('Write how many grams of coffee beans do you want to add:'))
    cups_stock += int(input('Write how many disposable cups of coffee do you want to add:'))


def trigger_action(action_to_trigger):
    if action_to_trigger == 'buy':
        beverage = choose_beverage()
        if isinstance(beverage, int):
            brew(beverage)
    elif action_to_trigger == 'fill':
        fill()
    elif action_to_trigger == 'take':
        take()
    elif action_to_trigger == 'remaining':
        remaining()


action = ''
while action != 'exit':
    action = choose_action()
    trigger_action(action)
