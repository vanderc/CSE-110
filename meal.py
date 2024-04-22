child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))
print(1 * '\n')

subtotal_amount = (child_meal * children) + (adult_meal * adults)
print('subtotal: ${:.2f}' .format(subtotal_amount))

sales_tax = (subtotal_amount * (tax/100))
print('Sales Tax: ${:.2f}' .format(sales_tax))

total = subtotal_amount + sales_tax
print('Total: ${:.2f}'.format(total))
print(1 * '\n')

payment = float(input('What is the payment amount? '))
change = (payment - total)
print('Change: ${:2f}'.format(change))