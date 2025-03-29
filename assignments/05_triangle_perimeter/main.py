def main():
    side1: float = float(input("What is the length of side 1? "))
    
    side2: float = float(input("What is the length of side 2? "))
    
    side3: float = float(input("What is the length of side 3? "))
    
    perimeter: float = side1 + side2 + side3
    
    print("The perimeter of the triangle is", perimeter)

if __name__ == '__main__':
    main()