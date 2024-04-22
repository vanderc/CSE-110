word = 'temples'
 

 
 
print("Guess the characters")
 
guesses = ''
 
attempts = 0
turns = 10

 
while turns > 0:
 
    
    failed = 0
 

    for char in word:
        
        
        if char in guesses.lower():
            print(char.upper(), end= '')
 
        else:
            print("_ ", end='')
 
            
            failed += 1
 
    if failed == 0:
        attempts += 1
        print('\nCongratulations! You guessed it!')
 
       
        print(f'You guessed it in {attempts} guesses.')
        break
 
    
    print()
    guess = input("guess a character: ")
    
 
  
    guesses += guess


    if len(guess) > len(word):
        print('Sorry, the guess must have the same number of letters as the secret word.')
        

    if len(guess) < len(word):
        print('Sorry, the guess must have the same number of letters as the secret word.')   
        
    
   
     
 
   
    if guess.lower() not in word:
 
        turns -= 1
 
        attempts += 1
   
 
        
        print(f'You have {turns} more guesses')
 
        if turns == 0:
            print('You ran out of attempts.')

 
   

        

#I feel like it is some where between 3 and 5 on the rating because I was not able to figure out everything but I think I did a good job. But I thought it might be cool to have a specific amount of guesses available.