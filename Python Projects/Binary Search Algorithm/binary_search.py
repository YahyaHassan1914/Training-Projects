def binary_search(arr, target):
    # Sort the array first
    arr.sort()
    
    left, right = 0, len(arr) - 1
    step = 1  # Initialize step counter
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: Searching in {arr[left:right + 1]}")
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid  # Found the target
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half
        step += 1  # Increment step counter

    print(f"{target} not found in the array")
    return -1  # Target not found

def main():
    # Input from user
    try:
        arr = list(map(int, input("Enter array elements separated by space: ").split()))
        target = int(input("Enter target element to search for: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return
    
    # Perform binary search after sorting
    result = binary_search(arr, target)
    
    # Output results
    if result != -1:
        print(f"Element {target} is present at index {result}")
    else:
        print(f"Element {target} is not present in the array")

if __name__ == "__main__":
    main()