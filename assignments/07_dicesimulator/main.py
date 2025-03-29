import random  

def main():
    for roll in range(3):  

        die1: int = random.randint(1, 6)

        die2: int = random.randint(1, 6)
        
        print("Roll #", roll + 1, ":", "Die 1 =", die1, "Die 2 =", die2)

if __name__ == '__main__':
    main()