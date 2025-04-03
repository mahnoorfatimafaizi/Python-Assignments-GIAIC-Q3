def double_list(numbers: list[float]) -> None:

    for i in range(len(numbers)):
        numbers[i] *= 2  

def main():

    numbers: list[float] = [1, 2, 3, 4]
    
    print("Original list:", numbers)
    
    double_list(numbers)
    
    print("Doubled list:", numbers)

if __name__ == "__main__":
    main()