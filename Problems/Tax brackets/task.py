def get_percentage(base_income):
    if 0 <= base_income <= 15527:
        return 0
    elif 15528 <= base_income <= 42707:
        return 0.15
    elif 42708 <= base_income <= 132406:
        return 0.25

    return 0.28


def calculate_tax(base_income, tax_percentage):
    return int(round(base_income * tax_percentage))


income = int(input())
percentage = get_percentage(income)
tax = calculate_tax(income, percentage)
print(f"The tax for {income} is {int(percentage * 100)}%. That is {tax} dollars!")
