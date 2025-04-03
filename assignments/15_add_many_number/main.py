def sum_list(numbers: list[float]) -> float:

    total: float = 0
    
    for num in numbers:
        total += num
    
    return total

def main():

    test_list: list[float] = [1.5, 2.0, 3.7, 4.2]
    result: float = sum_list(test_list)
    print("The sum of", test_list, "is", result)

if __name__ == '__main__':
    main()