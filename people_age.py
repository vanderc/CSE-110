people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
yougest_age = 99999
youngest_name = ''
for person_line in people:
    parts = person_line.split()
    name = parts[0]
    age = int(parts[1])
    if age < yougest_age:
        yougest_age = age
        youngest_name = name

print(f'The youngest person is {youngest_name} with an age of {yougest_age}')