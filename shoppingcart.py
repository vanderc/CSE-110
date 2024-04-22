cart = {}
print("Welcome to the Shopping Cart Program!")
 
while True:
    print()
    print ('Please type in one of these')
    print ('1. Add item ')
    print ('2. View cart ')
    print ('3. Remove Item ')
    print ('4 compute total')
    print ('5 quit')
  
    select = int(input(' Type in a number to go on '))
 
    if select == 1:
        item = input(' What item would you like to add?  ')
        price = float(input(' type in the price '))
        cart [item] = price
        print(f"'{item}' has been added to your cart.")
        print(f' The price is ${price:.2f}')
 
    if select == 2:
        print('The contents of the shopping cart are: ')
        for item in cart:
            print(f'  {item} - ${cart [item]:.2f}')
            #I couldn't get the items to display with the numbers without messing up the list of items.
    if select == 3:
        takeout = input('Which item would you like to remove?(type the item)  ')
        cart.pop(takeout)
        #works if you type in the item word
    if select == 4:
        total = 0
        for item in cart:
            total += cart [item]
        print(f' ${total:.2f}')
 
    if select == 5:
        print ('Thank you, goodbye.')
        break

#I think that I would say it is a 4 because I was able to figure out almost everything. I could not figure out how to properly get the view cart menu to be numbered but the remove item works if you type out the item. I did add some extras.