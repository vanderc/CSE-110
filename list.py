clients = []

new_client = ''
while new_client != 'quit':
    new_client = input('What is the name of a client? ')
    
    #This removes the quit from the list
    if new_client != 'quit':
        clients.append(new_client)

for client in clients:
    print(client)

print()

tips = [12.25, 13.95, 8.50]

running_total = 0

for tip_amount in tips:
    #running_total = running_total + tip_amount
    running_total += tip_amount


print(f'The total is: {running_total:.2f}')