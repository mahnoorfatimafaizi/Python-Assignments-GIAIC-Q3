import random  

def main():

    secret_number: int = random.randint(0, 99)
    
    guess: int = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))
    
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high")

            print("Your guess is too low")
        
        guess = int(input("Enter a new number: "))
    
    print("Congrats! The number was:", secret_number)

if __name__ == '__main__':
    main()
