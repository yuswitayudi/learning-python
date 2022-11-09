trying = 0
secret_number = 7
limit = 3


while trying < limit:
    guess_number = input("Please insert your number (1-10): ")
    guess_number = int(guess_number)
    
    if guess_number == secret_number:
        print("You win my bro")
        break
        
    trying += 1