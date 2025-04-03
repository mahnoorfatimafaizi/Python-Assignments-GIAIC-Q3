def add_three_copies(my_list: list[str], data: str) -> None:

    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    message: str = input("Enter a message to copy: ")
    
    test_list: list[str] = []
    
    print("List before:", test_list)
    
    add_three_copies(test_list, message)
    
    print("List after:", test_list)

if __name__ == "__main__":
    main()