import random

def main():
    for roll in range(3):  

        die1: int = random.randint(1, 6)

        die2: int = random.randint(1, 6)

        total: int = die1 + die2
        
        print("Roll", roll + 1)
        print("Die 1:", die1)
        print("Die 2:", die2)
        print("Total:", total)
        print()  

if __name__ == '__main__':
    main()