"""def calculate_tax(value):
    return value * 0.3


price = float(input('Write the price of service: '))
print(f'The price of tax is {calculate_tax(price)}, so the remainder is {price - calculate_tax(price)}')"""

"""price = float(input('Enter the price of service: '))
tax = lambda x: x * 0.4
print(tax(price))"""

price2 = [100, 300, 20, 50]
tax2 = list(map(lambda x: x * 2, price2))
print(tax2)
