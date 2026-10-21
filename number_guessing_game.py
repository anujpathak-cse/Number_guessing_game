import random

while True:
     

    secret_number = random.randint(1, 100)
    
    attempt = 0
    while True:

        guess_number = int(input("Guess a number between 1 to 100: "))
        attempt = attempt + 1
      

        if guess_number < secret_number:
            print("Too low! Try again.")

        elif secret_number < guess_number:
            print("Too high! Try again.")

        elif secret_number == guess_number:
            print("Congratulations! You guessed the correct number.")
       

            print("Number of attempts:", attempt)

            break
        if attempt >= 7:
            print("Sorry, you've reached the maximum number of attempts")
            exit()
                    
    while True:

        retry = (input("Do you want to play again? (yes/no): ")).lower()

        if retry == "yes":
            break
        elif retry == "no": 
            print("Thanks for playing!")
            break
    
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        
            continue
    if retry == "no":   
        break