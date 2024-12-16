import random

# func release the game "guess_number"
def guess_number():
    # Generates a random number between 1 and 100
    rand_num = random.randint(1, 100)
    
    # Prompts the user to input a number
    user_num = int(input("Enter number: "))
    
    # Repeats until the user guesses the random number correctly
    while user_num != rand_num:
        # Provides feedback if the guess is too high or too low
        if user_num > rand_num:
            user_num = int(input("Too high. Enter number: "))
        else:
            user_num = int(input("Too low. Enter number: "))
    
    # Congratulates the user upon correct guess
    print(f"Congratulates! You guessed the number {rand_num}")


guess_number()
