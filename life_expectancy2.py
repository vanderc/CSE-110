with open('life_expectancy.csv') as file:

    
    entities = []
    codes = []
    years = []
    life_expectancies =[]

   
    for line in file:
        line_stripped = line.strip()
        line_splited = line_stripped.split(',')
        
        
       
        codes.append(line_splited[1])
        life_expectancies.append(line_splited[3])
        
    
    max_life_exp = max(life_expectancies[1:])
    max_index = life_expectancies.index(max_life_exp) 
     

    print(f'The overall max life expectancy is: {max_life_exp}')

   
    min_life_exp = min(life_expectancies[1:])
    min_index = life_expectancies.index(min_life_exp)
    

    print(f'The overall min life expectancy is: {min_life_exp}')

# I was able to complete all of the required steps for the milestone assignment. It loads the data set, line by line iteration, line splitting, and the lowest and highest values.