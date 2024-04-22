print('Welcome to the Shopping Cart Program!')
cart = []
prices = []
total = []
total_price = []
sum = 0
while True:
    print()
    print ('Please type in one of these')
    print ('1. Add item ')
    print ('2. View cart ')
    print ('3. Remove Item ')
    print ('4 compute total')
    print ('5. quit')
 
    select = int(input('Type in a number to go on: '))
    item = ""
    if select == 1:
        while item != 'ok':
            item = input('What item would you like to add? ')
            price = float(input('What is the price: '))
            prices.append(price)
             
            
            cart.append(item)
            print(f"'{item}' has been added to the cart.")
            print(f' The price is ${price:.2f}')
            break
    
            
    if select == 2:
        print('The contents of the shopping cart are: ')
        for item in cart:
            print(f'  {item} - ${cart :.2f}')        
   
     
                     
    if select == 3:
        takeout = input('Which item would you like to remove? ')
        cart.remove(takeout)
        continue
         
     
    if select == 4:
        for price in total_price:
            sum += price
            print(sum(total_price))
            break
             
             
         
    if select == 5:
        print ('Thank you goodbye.')
        break

#I was able to complete the steps of adding an item and price to the list, able to display the list of items without the prices right now, able to remove items if you spell out the item name.


