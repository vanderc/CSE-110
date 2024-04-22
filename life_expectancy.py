with open('life_expectancy.csv') as file:
    next(file)

    entities = []
    years = []
    life_expect = []

    index = 0
    user_entities = []
    user_years = []
    user_life_expectancy = []

    highest_life_entity = ''
    highest_life = 0
    highest_year = 0


    lowest_life_entity = ''
    lowest_life = 9999
    lowest_year = 9999


    for line in file:
        line_stripped = line.strip()
        line_splited = line_stripped.split(',')
        
        
        entities.append(line_splited[0])
        years.append(int(line_splited[2]))
        life_expect.append(float(line_splited[3]))

    
    for i in range(len(entities)):
        
        entity = entities[i]
        max_life = life_expect[i]
        min_life = life_expect[i]
        year = years[i]

        if max_life > highest_life: 
            highest_life = max_life
            highest_life_entity = entity
            highest_year = year

        elif min_life < lowest_life: 
            lowest_life = min_life
            lowest_life_entity = entity
            lowest_year = year
    
    
    print(f'The overall max life expectancy is: {highest_life:.2f} from {highest_life_entity} in {highest_year}')
    print(f'The overall min life expectancy is: {lowest_life:.2f} from {lowest_life_entity} in {lowest_year}')

    
    highest_life_entity = ''
    highest_life = 0
    highest_year = 0

    lowest_life_entity = ''
    lowest_life = 9999
    lowest_year = 9999

    user_input = int(input('\nEnter a year of interest: '))
    
    for i in years: 
        if i == user_input:

            user_entities.append(entities[index])
            user_years.append(int(years[index]))
            user_life_expectancy.append(float(life_expect[index]))
        
        index += 1

    
    for i in range(len(user_life_expectancy)):
        
        entity = user_entities[i]
        max_life, min_life = user_life_expectancy[i], user_life_expectancy[i]

        if max_life > highest_life: 
            highest_life = max_life
            highest_life_entity = entity

        
        if min_life < lowest_life: 
            lowest_life = min_life
            lowest_life_entity = entity

         
    avarage = sum(user_life_expectancy) / len(user_life_expectancy)
    print(f'IN {user_input} INFO: ')
    print(f'The avarage life expectancy across all countries was {avarage:.2f}')
    print(f'The max life expectancy was in {highest_life_entity} with {highest_life:.2f}')
    print(f'The min life expectancy was in {lowest_life_entity} with {lowest_life:.3f}')

    index = 0
    user_entities = []
    user_years = []
    user_life_expectancy = []

    highest_life_entity = ''
    highest_life = 0
    highest_year = 0

    lowest_life_entity = ''
    lowest_life = 9999
    lowest_year = 9999  

    
    user_input = input('\nEnter a country of interest: ')

    for i in entities: 

        if i == user_input.title():

            user_entities.append(entities[index])
            user_years.append(int(years[index]))
            user_life_expectancy.append(float(life_expect[index]))
        
        index += 1

   
    for i in range(len(user_life_expectancy)):
        
        entity = user_entities[i]
        max_life, min_life = user_life_expectancy[i], user_life_expectancy[i]

        if max_life > highest_life: 
            highest_life = max_life
            highest_life_entity = entity

        
        if min_life < lowest_life:
            lowest_life = min_life
            lowest_life_entity = entity


    avarage = sum(user_life_expectancy) / len(user_life_expectancy)     
    print(f'IN {user_input.upper()} OVERALL INFO: ')
    print(f'The overall life expectancy is {avarage:.2f}')
    print(f'The max life expectancy was in {highest_life_entity} with {highest_life:.2f}')
    print(f'The min life expectancy was in {lowest_life_entity} with {lowest_life:.2f}')

    
# 5- I am pretty sure that I met all the requirements and I was able to give the ability to see the results from a country of the users choice.