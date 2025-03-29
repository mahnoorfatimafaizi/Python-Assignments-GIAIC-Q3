def main():
    number: float = float(input("Type a number to see its square: "))
    
    square: float = number * number
    
    print(number, "squared is", square)

if __name__ == '__main__':
    main()