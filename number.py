first = int(input('What is the first number? '))
second = int(input('What is the second number? '))

if first > second:
    print('The first nuber is greater')
else:
    print('The first nuber is not greater')

if first == second:
    print('The numbers are equal')
else:
    print('The nubers are not equal')

if first < second:
    print('The second number is greater')
else:
    print('The second number is not greater')

print()

user_animal = input('What is your favorite animal? ')

if user_animal.lower() == 'lion':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')