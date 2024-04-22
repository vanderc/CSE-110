items = ['crayon', 'scissors', 'paper', 'glitter glue', 'markers', 'pens']

for item in items:
    print(f'The item is: {item}')

print()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = range(10)

for number in range(10):
    print(number)
print()

for i in range(100, 200):
    print(i)
print()

for i in range(100, 200, 10):
    print(i)

print()

for i in range(5):
    print(i)

print()

for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f'--{j}')

print()

first_name = 'Brigham'
for letter in first_name:
    print(f'The letter is: {letter}')

print()

word = 'books'
number_of_letters = len(word)

for index in range(number_of_letters):
    letter = word[index]
    print(f'Index: {index} Letter: {letter}')

print()

dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")

print()

first_name = 'Brigham '

for i, letter in enumerate(first_name):
    print(f'The letter {letter} is at position {i}')

    


