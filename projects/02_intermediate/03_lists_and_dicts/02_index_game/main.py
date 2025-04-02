def access_element(lst: list, index: int) -> str:

    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    return "Error: Index out of range"

def modify_element(lst: list, index: int, value: str) -> str:

    if 0 <= index < len(lst):
        old_value = lst[index]
        lst[index] = value
        return f"Replaced {old_value} with {value} at index {index}"
    return "Error: Index out of range"

def slice_list(lst: list, start: int, end: int) -> str:

    if start < 0 or end > len(lst) or start > end:
        return "Error: Invalid start or end index"
    return f"Slice from {start} to {end}: {lst[start:end]}"

def main():

    game_list: list = [42, "cat", 3.14, "dog", 99, "bird"]
    print("Starting list:", game_list)
    

    while True:
        print("\nOptions: 'access', 'modify', 'slice', or 'quit'")
        choice: str = input("What would you like to do? ").lower()
        
        if choice == "quit":
            print("Thanks for playing!")
            break
        
        elif choice == "access":
            index: int = int(input("Enter an index: "))
            result: str = access_element(game_list, index)
            print(result)
            print("Current list:", game_list)
        
        elif choice == "modify":
            index: int = int(input("Enter an index: "))
            value: str = input("Enter a new value: ")
            result: str = modify_element(game_list, index, value)
            print(result)
            print("Current list:", game_list)
        
        elif choice == "slice":
            start: int = int(input("Enter start index: "))
            end: int = int(input("Enter end index: "))
            result: str = slice_list(game_list, start, end)
            print(result)
            print("Current list:", game_list)
        
        else:
            print("Invalid option, try again")

if __name__ == "__main__":
    main()