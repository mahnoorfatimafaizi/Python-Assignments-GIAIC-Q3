def main():
    fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))
    
    celsius: float = (fahrenheit - 32) * 5.0 / 9.0
    
    print("Temperature:", fahrenheit, "F =", celsius, "C")

if __name__ == '__main__':
    main()