def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    target1 = 23
    target2 = 15
    
    result1 = binary_search(numbers, target1)
    if result1 != -1:
        print(f"Found {target1} at index {result1}")
    else:
        print(f"{target1} not found in the list")
    
    result2 = binary_search(numbers, target2)
    if result2 != -1:
        print(f"Found {target2} at index {result2}")
    else:
        print(f"{target2} not found in the list")