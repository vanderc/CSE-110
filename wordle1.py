

 

 
word = 'temple'
 

 
 
print("Guess the characters")
 
guesses = ''
 
attempts = 0
turns = 12
 
 
while turns > 0:
 
    
    failed = 0
 
    
    for char in word:
 
        
        if char in guesses:
            print(char, end= '')
 
        else:
            
 
            
            failed += 1
 
    if failed == 0:
        attempts += 1
        print('\nCongratulations! You guessed it!')
 
       
        print(f'You guessed it in {attempts} guesses.')
        break
 
    
    print()
    guess = input("guess a character:")
 
  
    guesses += guess
 
  
    if guess not in word:
 
        turns -= 1
        attempts += 1
      
        print('Try again')
 
        
        print('You have', + turns, 'more guesses')
 
        if turns == 0:
            print('You ran out of attempts.')

#I think I did good on this. I am not sure how the display of wrong amounts of letters in the guess works and continues with the loop.